import requests

from ..constants import HTTP_RESPONSE_CODE


class Resource(object):

    @classmethod
    def get_url(cls, url):
        response = requests.get(url)
        if response.status_code == HTTP_RESPONSE_CODE.OK :
            return response.json()
        else:
            raise ServerError(response.text)


class ServerError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(ServerError, self).__init__(message)
