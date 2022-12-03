from .entities import Entry, EntryHistory


def entity(entity_data) -> Entry:
    return Entry(entity_data)


def entity_history(entity_history_data) -> EntryHistory:
    return EntryHistory(entity_history_data)
