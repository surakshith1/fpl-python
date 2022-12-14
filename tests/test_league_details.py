import unittest
from fpl import LeagueDetails


class TestLeagueDetails(unittest.TestCase):
    def test_entry(self):
        league_details = LeagueDetails().fetch(4194, page_standings=2)
        self.assertEqual(league_details.league.id, 4194)


if __name__ == '__main__':
    unittest.main()