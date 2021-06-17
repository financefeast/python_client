

class Response(object):

    def __init__(self, payload):
        self._payload = payload

    def __repr__(self):
        """
        Returns a dict of class attributes
        """
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)

    @property
    def data(self):
        try:
            return self._payload['data']
        except KeyError:
            return []

    @property
    def token(self):
        try:
            return self._payload['access_token']
        except KeyError:
            return None