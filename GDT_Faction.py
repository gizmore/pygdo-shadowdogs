from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.GDO_Player import GDO_Player


class GDT_Faction(GDT_Enum):

    BONUS = {
        'freeborn': {'bod': 10, 'mag': 10, 'str': 4, 'int': 5, 'dex': 5, 'qui': 5, 'cha': 5, 'tra': 5, 'hac': 8, 'cry': 9, 'mat': 9, 'fig': 0},
        'consort': {'bod': 10, 'mag': 10, 'str': 4, 'int': 5, 'dex': 5, 'qui': 5, 'cha': 5, 'tra': 5, 'hac': 6, 'cry': 7, 'mat': 7, 'fig': 0},
        'seeker': {'bod': 10, 'mag': 10, 'str': 4, 'int': 6, 'dex': 5, 'qui': 5, 'cha': 6, 'tra': 5, 'hac': 7, 'cry': 8, 'mat': 8, 'fig': 7},
        'aegis': {'bod': 10, 'mag': 10, 'str': 6, 'int': 5, 'dex': 5, 'qui': 5, 'cha': 4, 'tra': 5, 'hac': 5, 'cry': 6, 'mat': 6, 'fig': 10},
    }

    def gdo_choices(self) -> dict:
        return {
            'freeborn': 'Freeborn',
            'council': 'Council',
            'seekers': 'Seekers',
            'aegis': 'Aegis',
        }

    def apply(self, player: GDO_Player):
        player.modify(self.BONUS[self.get_val()])
