from gdo.core.GDT_Enum import GDT_Enum
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player


class GDT_Race(GDT_Enum):

    BONUS: dict[str,dict[str,int]] = {
        'dragon':   {},
        'animal':   {},
        'drone':    {},

        'elve':     {'bod': 0, 'mag': 1, 'str': 1, 'dex': 1, 'qui': 1, 'int': 6, 'wis': 2, 'cha': 2},
        'halfelve': {'bod': 1, 'mag': 1, 'str': 2, 'dex': 1, 'qui': 1, 'int': 5, 'wis': 1, 'cha': 1},
        'human':    {'bod': 1, 'mag': 0, 'str': 3, 'dex': 1, 'qui': 1, 'int': 4, 'wis': 1, 'cha': 1},
        'dwarf':    {'bod': 2, 'mag': 0, 'str': 4, 'dex': 1, 'qui': 0, 'int': 3, 'wis': 1, 'cha': 0},
        'halforc':  {'bod': 2, 'mag':-1, 'str': 5, 'dex': 0, 'qui': 0, 'int': 2, 'wis': 0, 'cha': 0},
        'orc':      {'bod': 2, 'mag':-2, 'str': 6, 'dex': 0, 'qui': 0, 'int': 1, 'wis': 0, 'cha': 0},
        'troll':    {'bod': 3, 'mag':-3, 'str': 7, 'dex': 0, 'qui': 0, 'int': 0, 'wis': 0, 'cha': 0},
    }

    GENDER: dict[str,dict[str,int]] = {
        'male':   {'bod': 1, 'str': 1},
        'female': {'mag': 1, 'int': 1, 'cha': 2},
    }

    _npcs: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._npcs = False

    def npcs(self, npcs: bool=True):
        self._npcs = npcs
        return self

    def gdo_choices(self) -> dict:
        races = {
            'elve': 'Elve',
            'halfelve': 'Halfelve',
            'human': 'Human',
            'dwarf': 'Dwarf',
            'halforc': 'Halforc',
            'orc': 'Orc',
        }
        if self._npcs:
            races.update({
                'dragon': 'Dragon',
                'animal': 'Animal',
                'drone': 'Drone',
            })
        return races

    def apply(self, player: 'GDO_Player'):
        bonus = self.BONUS[self.get_val()]
        for key, val in bonus.values():
            player.apply(f"p_{key}", val)
        bonus = self.GENDER[player.gdo_val('p_gender')]
        for key, val in bonus.values():
            player.apply(f"p_{key}", val)
