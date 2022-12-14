from .entities import Entry, EntryHistory, LeagueDetails


def entity(entity_data) -> Entry:
    return Entry(entity_data)


def entity_history(entity_history_data) -> EntryHistory:
    return EntryHistory(entity_history_data)


def league_details(league_details_data) -> LeagueDetails:
    return LeagueDetails(league_details_data)
