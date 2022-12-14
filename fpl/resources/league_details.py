from ..constants.url import URL
from .base import Resource
from . import utils as util


class LeagueDetails:

    def __init__(self):
        self.base_url = URL.LEAGUE_DETAILS_URL

    def fetch(self, league_id, page_new_entries=1, page_standings=1):
        url = f"{self.base_url}?page_new_entries={page_new_entries}&page_standings={page_standings}".format(league_id)
        response = Resource.get_url(url)
        return util.league_details(response)
