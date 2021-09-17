from financefeast.common import EnvironmentsStream
from websocket import (
    create_connection, WebSocketException, WebSocketConnectionClosedException, WebSocketBadStatusException, WebSocketApp, enableTrace
)
import logging
import time
import json
from ssl import SSLError

class Stream(object):
    DEFAULT_LOG_LEVEL = logging.INFO
    DEFAULT_SOCKET_HEADER = None

    def __init__(self, token:str, logger:logging.Logger = None, environment:EnvironmentsStream=EnvironmentsStream.local):

        self._token = token
        self._logger = logger
        self._environment = environment
        self._websocket = None

        if not logger:
            self._logger = logging.getLogger('ff_stream')

        # set log level
        logging.basicConfig(level=self.DEFAULT_LOG_LEVEL)

        self._logger.info(f"API environment set as {self._environment.name}")

    def connect(self):
        """
        Creates inital websocket connection
        :return:
        """
        self._create_connection()


    def _create_connection(self):
        """
        Creates actual socket connection
        :return:
        """
        while True:
            try:
                enableTrace(False)
                self._websocket = WebSocketApp(self._environment.value,
                                          on_message = self._on_message,
                                          on_error = self._on_error,
                                          on_close = self._on_close,
                                          header=self.DEFAULT_SOCKET_HEADER)
                self._websocket.on_open = self._on_open
                self._websocket.run_forever(skip_utf8_validation=True,ping_interval=10,ping_timeout=8)
            except Exception as e:
                self._logger.exception("Websocket connection Error  : {0}".format(e))
            self._logger.info("Reconnecting websocket after 5 sec")
            time.sleep(5)

    def _on_open(self, wsapp):
        """
        Handle socket open
        Send authentication
        :return:
        """
        self._send({"type": "authenticate",
                    "data": {
                        "token": self._token
                    }})


    def _on_error(self, wsapp, err):
        """
        Handle socket error
        :return:
        """
        self._logger.error(f"{err}")

    def _on_close(self, wsapp, close_status_code, close_msg):
        """
        Handle socket close
        :return:
        """
        if close_status_code and close_msg:
            self._logger.info(f"{close_msg} : {close_status_code}")

    def _on_message(self, wsapp, message):
        """
        Returns data or empty string ''
        :return:
        """

        self._logger.info(f"Received message {message}")
        return json.dumps(message.decode("utf-8"))

    def _send(self, data):
        """
        Send data to the websocket
        :param data:
        :return:
        """
        data = json.dumps(data)
        if self._websocket:
            self._websocket.send(data)

    def _ping(self):
        return self._send({'type': 'ping'})