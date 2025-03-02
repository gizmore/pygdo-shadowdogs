from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.GDO_Player import GDO_Player


class GDT_Faction(GDT_Enum):

    BONUS = {
        'freeborn': {},
        'council': {},
        'seekers': {},
        'aegis': {},
    }

    def gdo_choices(self) -> dict:
        return {
            'freeborn': 'Freeborn',
            'council': 'Council',
            'seekers': 'Seekers',
            'aegis': 'Aegis',
        }

    def apply(self, player: GDO_Player):
        player.modify(self.BONUS[player.gdo_val('p_faction')])
