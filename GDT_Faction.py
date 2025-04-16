from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

from gdo.core.GDT_Enum import GDT_Enum


class GDT_Faction(GDT_Enum):

    FREEBORN = 'freeborn' # creators and artists of ESL.
    CONSORT = 'consort' # accepting current state of minds.
    SEEKER = 'seekers' # running for truth.
    AEGIS = 'aegis' # Military and right-winged people.

    BONUS = {
        'freeborn': {'int': 5, 'wis': 2, 'dex': 1, 'qui': 1, 'hac': 5},
        'consort': {'mag': 3, 'cha': 1, 'tra': 10},
        'seeker': {}, # all start fresh.
        'aegis': {'bod': 1, 'str': 1, 'fig': 2, 'attack': 5, 'dex': 2, 'qui': 2},
    }

    def gdo_choices(self) -> dict:
        return {
            'freeborn': 'Freeborn',
            'council': 'Council',
            'seekers': 'Seekers',
            'aegis': 'Aegis',
        }

    def apply(self, player: 'GDO_Player'):
        player.modify(self.BONUS[self.get_val()])
