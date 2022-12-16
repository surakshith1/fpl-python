class Entry:
    def __init__(self, data):
        self.id = data.get("id", None)
        self.joined_time = data.get("joined_time", None)
        self.started_event = data.get("started_event", None)
        self.favourite_team = data.get("favourite_team", None)
        self.player_first_name = data.get("player_first_name", None)
        self.player_last_name = data.get("player_last_name", None)
        self.player_region_id = data.get("player_region_id", None)
        self.player_region_name = data.get("player_region_name", None)
        self.player_region_iso_code_short = data.get("player_region_iso_code_short", None)
        self.player_region_iso_code_long = data.get("player_region_iso_code_long", None)
        self.summary_overall_points = data.get("summary_overall_points", None)
        self.summary_overall_rank = data.get("summary_overall_rank", None)
        self.summary_event_points = data.get("summary_event_points", None)
        self.summary_event_rank = data.get("summary_event_rank", None)
        self.current_event = data.get("current_event", None)
        self.name = data.get("name", None)
        self.name_change_blocked = data.get("name_change_blocked", None)
        self.kit = data.get("kit", None)
        self.last_deadline_bank = data.get("last_deadline_bank", None)
        self.last_deadline_value = data.get("last_deadline_value", None)
        self.last_deadline_total_transfers = data.get("last_deadline_total_transfers", None)
        self.leagues = data.get("leagues", {})


class EntryHistory:
    def __init__(self, data):
        self.current = []
        for current_data in data.get("current", []):
            self.current.append(self.GameWeekHistoryItem(current_data))

        self.past = []
        for past_data in data.get("past", []):
            self.past.append(self.PastHistoryItem(past_data))

        self.chips = []
        for chips_data in data.get("chips", []):
            self.chips.append(self.ChipItem(chips_data))

    class GameWeekHistoryItem:
        def __init__(self, data):
            self.event = data.get("event", None)
            self.points = data.get("points", None)
            self.total_points = data.get("total_points", None)
            self.rank = data.get("rank", None)
            self.rank_sort = data.get("rank_sort", None)
            self.overall_rank = data.get("overall_rank", None)
            self.bank = data.get("bank", None)
            self.value = data.get("value", None)
            self.event_transfers = data.get("event_transfers", None)
            self.event_transfers_cost = data.get("event_transfers_cost", None)
            self.points_on_bench = data.get("points_on_bench", None)

    class PastHistoryItem:
        def __init__(self, data):
            self.season_name = data.get("season_name", None)
            self.total_points = data.get("total_points", None)
            self.rank = data.get("rank", None)

    class ChipItem:
        def __init__(self, data):
            self.name = data.get("name", None)
            self.event = data.get("event", None)
            self.time = data.get("time", None)


class LeagueDetails:
    class NewEntries:
        def __init__(self, has_next, page, results):
            self.has_next = has_next
            self.page = page
            self.results = results

    class League:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    class Standings:
        def __init__(self, has_next, page, results):
            self.has_next = has_next
            self.page = page
            self.results = results

    def __init__(self, data):
        self.last_updated_data = data.get('last_updated_data', '')
        new_entries = data.get('new_entries', {})
        self.new_entries = self.NewEntries(
            new_entries.get('has_next', False),
            new_entries.get('page', 1),
            new_entries.get('results', [])
        )
        league = data.get('league', {})
        self.league = self.League(
            league.get('id', 0),
            league.get('name', '')
        )
        standings = data.get('standings', {})
        self.standings = self.Standings(
            standings.get('has_next', False),
            standings.get('page', 1),
            standings.get('results', [])
        )


class Fixtures:

    def __init__(self, json_response):
        self.fixtures = []
        for data in json_response:
            self.fixtures.append(self.Fixture(data))

    class Fixture:
        def __init__(self, data):
            self.code = data.get('code', 0)
            self.event = data.get('event', 0)
            self.finished = data.get('finished', False)
            self.finished_provisional = data.get('finished_provisional', False)
            self.id = data.get('id', 0)
            self.kickoff_time = data.get('kickoff_time', '')
            self.minutes = data.get('minutes', 0)
            self.provisional_start_time = data.get('provisional_start_time', False)
            self.started = data.get('started', False)
            self.team_a = data.get('team_a', 0)
            self.team_a_score = data.get('team_a_score', None)
            self.team_h = data.get('team_h', 0)
            self.team_h_score = data.get('team_h_score', None)
            self.stats = data.get('stats', [])
            self.team_h_difficulty = data.get('team_h_difficulty', 0)
            self.team_a_difficulty = data.get('team_a_difficulty', 0)
            self.pulse_id = data.get('pulse_id', 0)