from ..constants.url import URL
from .base import Resource
from . import utils as util


class Entry:

    def __init__(self):
        self.base_url = URL.ENTRY_URL

    def fetch(self, entry_id):
        url = "{}/{}".format(self.base_url, entry_id)
        response = Resource.get_url(url)
        return util.entity(response)
