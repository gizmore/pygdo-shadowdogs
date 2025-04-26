from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

from gdo.core.GDT_Enum import GDT_Enum


class GDT_Faction(GDT_Enum):

    FREEBORN = 'freeborn' # creators and artists of ESL.
    COUNCIL = 'council' # accepting current state of minds.
    SEEKER = 'seeker' # running for truth.
    AEGIS = 'aegis' # Military and right-winged people.

    BONUS = {
        'freeborn': {'int': 5, 'wis': 3, 'dex': 1, 'qui': 2, 'hac': 5},
        'council': {'mag': 3, 'cha': 1, 'tra': 20},
        'seeker': {}, # all start fresh.
        'aegis': {'bod': 1, 'str': 1, 'fig': 2, 'attack': 5, 'dex': 2, 'qui': 2},
    }

    def gdo_choices(self) -> dict:
        return {
            'freeborn': 'Freeborn',
            'council': 'Council',
            'seeker': 'Seeker',
            'aegis': 'Aegis',
        }

    def apply(self, player: 'SD_Player'):
        player.modify(self.BONUS[self.get_val()])
