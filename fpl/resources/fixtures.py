from ..constants.url import URL
from .base import Resource
from . import utils as util


class Fixtures:

    def __init__(self):
        self.base_url = URL.FIXTURES_URL

    def fetch(self, event=None):
        url = "{}".format(self.base_url)
        if event:
            url += "?event="+ str(event)
        response = Resource.get_url(url)
        return util.fixtures(response)
