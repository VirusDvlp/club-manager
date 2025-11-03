from enum import Enum


from text import (
    get_french_club_card_text,
    get_buisness_meet_card_text,
    get_table_game_card_text,
    get_women_meets_card_text,
)


class EventType(Enum):
    FRENCH_CLUB = 0
    TABLE_GAMES = 1
    BUISNESS_MEETS = 2
    WOMEN_MEETS = 3
    INITIATIVE = 4


    def get_card_text(self, **kwargs):
        functions = {
            EventType.FRENCH_CLUB: get_french_club_card_text,
            EventType.BUISNESS_MEETS: get_buisness_meet_card_text,
            EventType.TABLE_GAMES: get_table_game_card_text,
            EventType.WOMEN_MEETS: get_women_meets_card_text

        }

        return functions[self](**kwargs)
