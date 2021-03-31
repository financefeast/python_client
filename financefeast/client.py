import os
import logging
import requests
from enum import Enum
from functools import lru_cache

FF_LOGIN_URI = "oauth/login"

class Environments(Enum):
    test = "https://api.test.financefeast.io"
    prod = "https://api.financefeast.io"

class FinanceFeast:

    DEFAULT_LOG_LEVEL = logging.DEBUG

    def __init__(self, client_id:str = None, client_secret:str = None, logger:logging.Logger = None, environment:Environments=Environments.test.value):
        self._client_id = client_id
        self._client_secret =client_secret
        self._logger = logger
        self._environment = environment
        self._access_token = None

        if not logger:
            self._logger = logging.getLogger('ff_client')

        # set log level
        logging.basicConfig(level=self.DEFAULT_LOG_LEVEL)

        self._requests = self.RequestRateLimited(self._logger)

        if not self._client_id:
            self._client_id = os.environ.get('FF-CLIENT-ID')
        if not self._client_secret:
            self._client_secret = os.environ.get('FF-CLIENT-SECRET')

        if not self._client_secret:
            raise Exception(
                "parameter `client_id` must be either passed or set as an environment variable 'FF-CLIENT-ID'"
            )

        if not self._client_id:
            raise Exception(
                "parameter `client_secret` must be either passed or set as an environment variable 'FF-CLIENT-SECRET'"
            )

        self._logger.debug(f'Authorizing to Financefeast API environment {self._environment}')
        self.__authorize()

    def __authorize(self):
        """
        Authorize client credentials
        :return: access token
        """
        if not self._access_token:
            url = f'{self._environment}/{FF_LOGIN_URI}'
            self._logger.debug(f'Constructed url {url} for authorization')

            headers = {"X-FF-ID": self._client_id, "X-FF-SECRET": self._client_secret}

            payload = self._requests.get(url=url, headers=headers)

            try:
                self._access_token = payload['access_token']
                self._logger.debug('Found a valid access_token')
            except KeyError:
                self._logger.exception(f'{payload["detail"]}')
                raise Exception(
                    f'{payload["detail"]}'
                )

            self._logger.info("Client successfully authorized to API")

        return self._access_token

    def _generate_authorization_header(self):
        return {'Authorization': f'Bearer: {self._access_token}'}


    """
        Endpoint methods below
    """

    def alive(self):
        """
        Call health/alive endpoint to get health of the API
        :return:
        """
        url = url = f'{self._environment}/health/alive'
        headers = self._generate_authorization_header()

        r = self._requests.get(url=url, headers=headers)

        return r

    def tickers(self):
        """
        Call info/ticker endpoint to get a list of supported tickers
        :return:
        """
        url = url = f'{self._environment}/info/ticker'
        headers = self._generate_authorization_header()

        r = self._requests.get(url=url, headers=headers)

        try:
            data = r['data']
        except KeyError:
            data = r['error']

        return data

    def exchanges(self):
        """
        Call info/exchange endpoint to get a list of supported exchanges
        :return:
        """
        url = url = f'{self._environment}/info/exchange'
        headers = self._generate_authorization_header()

        r = self._requests.get(url=url, headers=headers)

        try:
            data = r['data']
        except KeyError:
            data = r['error']

        return data


    class RequestRateLimited():
        TIMEOUT_CONN = 1.5
        TIMEOUT_RESP = 1.5
        RATE_LIMIT_HEADER_LIMIT_NAME = 'x-ratelimit-limit'
        RATE_LIMIT_HEADER_REMAINING_NAME = 'x-ratelimit-remaining'
        RATE_LIMIT_HEADER_RESET_NAME = 'x-ratelimit-reset'

        def __init__(self, logger:logging.Logger = None):
            self.logger = logger
            self.session = requests.Session()
            self.rate_limit = None
            self.rate_limit_remaining = None
            self.rate_limit_reset = None

        def __parse_request_rate_limit_headers(self, request):

            try:
                self.rate_limit = request.headers[self.RATE_LIMIT_HEADER_LIMIT_NAME]
                self.logger.debug(f"Rate limit is {self.rate_limit}")
            except KeyError:
                self.logger.debug(f'No request header found for {self.RATE_LIMIT_HEADER_LIMIT_NAME}')
                self.rate_limit = None

            try:
                self.rate_limit_remaining = request.headers[self.RATE_LIMIT_HEADER_REMAINING_NAME]
                self.logger.debug(f"Rate limit remaining is {self.rate_limit_remaining}")
            except KeyError:
                self.logger.debug(f'No request header found for {self.RATE_LIMIT_HEADER_REMAINING_NAME}')
                self.rate_limit_remaining = None

            try:
                self.rate_limit_reset = request.headers[self.RATE_LIMIT_HEADER_RESET_NAME]
                self.logger.debug(f"Rate limit reset at {self.rate_limit_reset}")
            except KeyError:
                self.logger.debug(f'No request header found for {self.RATE_LIMIT_HEADER_RESET_NAME}')
                self.rate_limit_reset = None

            return

        def get(self, *args, **kwargs):

            r = requests.get(*args, timeout=(self.TIMEOUT_CONN, self.TIMEOUT_RESP), **kwargs)

            # inspect rate limits
            self.__parse_request_rate_limit_headers(r)

            self.logger.debug(
                f'Request to {kwargs.get("url")} returned a {r.status_code} status code')

            if r.status_code == 403:
                raise Exception(
                    "Not authorized"
                )

            if r.status_code == 429:
                self.logger.error(f'Rate limited exceeded. {r.json()}')

            try:
                payload = r.json()
            except Exception as e:
                return None

            return payload