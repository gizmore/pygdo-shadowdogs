from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

from gdo.core.GDT_Enum import GDT_Enum


class GDT_Faction(GDT_Enum):

    FREEBORN = 'freeborn'
    CONSORT = 'consort'
    SEEKER = 'seekers'
    AEGIS = 'aegis'

    BONUS = {
        'freeborn': {'int': 5, 'dex': 1, 'qui': 1, 'hac': 2},
        'consort': {'mag': 1, 'cha': 1, 'tra': 10},
        'seeker': {},
        'aegis': {'bod': 1, 'str': 1, 'fig': 2, 'attack': 5},
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
