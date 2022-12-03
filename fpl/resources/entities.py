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
            self.current.append(GameWeekHistoryItem(current_data))

        self.past = []
        for past_data in data.get("past", []):
            self.past.append(PastHistoryItem(past_data))

        self.chips = []
        for chips_data in data.get("chips", []):
            self.chips.append(ChipItem(chips_data))


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
