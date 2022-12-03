from ..constants.url import URL
from .base import Resource
from . import utils as util


class PlayerEntry:

    def __init__(self):
        self.base_url = URL.PLAYER_ENTRY_URL

    def fetch(self, player_entry_id):
        url = "{}/{}".format(self.base_url, player_entry_id)
        response = Resource.get_url(url)
        return util.player_entity(response)
