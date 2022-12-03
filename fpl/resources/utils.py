from .entities import PlayerEntry


def player_entity(entity_data) -> PlayerEntry:
    return PlayerEntry(entity_data)
