from gdo.core.GDT_Enum import GDT_Enum
from typing import TYPE_CHECKING, Iterator, Tuple

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class GDT_Race(GDT_Enum):

    LEVEL_CONSTS = {
        'elve':     2.75,
        'halfelve': 2.53,
        'human':    2.44,
        'dwarf':    2.40,
        'halforc':  2.35,
        'orc':      2.30,
        'troll':    2.25,
    }

    BONUS: dict[str,dict[str,int]] = {
        'mob':      {},
        'animal':   {},
        'drone':    {},
        'dragon':   {},

        'elve':     {'bod': 0, 'mag': 2, 'str': 1, 'dex': 1, 'qui': 1, 'int': 6, 'wis': 2, 'cha': 2, 'max_hp': 1, 'max_mp': 5, 'min_dmg': 0, 'max_dmg': 0},
        'halfelve': {'bod': 1, 'mag': 1, 'str': 2, 'dex': 1, 'qui': 1, 'int': 5, 'wis': 1, 'cha': 2, 'max_hp': 1, 'max_mp': 2, 'min_dmg': 0, 'max_dmg': 1},
        'human':    {'bod': 1, 'mag': 0, 'str': 3, 'dex': 1, 'qui': 1, 'int': 4, 'wis': 1, 'cha': 1, 'max_hp': 2, 'max_mp': 1, 'min_dmg': 0, 'max_dmg': 1},
        'dwarf':    {'bod': 2, 'mag': 0, 'str': 4, 'dex': 1, 'qui': 0, 'int': 3, 'wis': 1, 'cha': 1, 'max_hp': 2, 'max_mp': 1, 'min_dmg': 0, 'max_dmg': 1},
        'halforc':  {'bod': 2, 'mag':-1, 'str': 5, 'dex': 0, 'qui': 0, 'int': 2, 'wis': 0, 'cha': 0, 'max_hp': 3, 'max_mp': 0, 'min_dmg': 1, 'max_dmg': 1},
        'orc':      {'bod': 2, 'mag':-2, 'str': 6, 'dex': 0, 'qui': 0, 'int': 1, 'wis': 0, 'cha': 0, 'max_hp': 3, 'max_mp': 0, 'min_dmg': 1, 'max_dmg': 2},
        'troll':    {'bod': 3, 'mag':-3, 'str': 7, 'dex': 0, 'qui': 0, 'int': 0, 'wis': 0, 'cha': 0, 'max_hp': 4, 'max_mp': 0, 'min_dmg': 2, 'max_dmg': 3},
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

    def all_bonuses(self, player: 'SD_Player') -> Iterator[Tuple[str, int]]:
        bonus = self.BONUS[self.get_val()]
        for key, val in bonus.items():
            yield key, val
        bonus = self.GENDER[player.gdo_val('p_gender')]
        for key, val in bonus.items():
            yield key, val

    def apply(self, player: 'SD_Player'):
        for key, val in self.all_bonuses(player):
            player.apply(f"p_{key}", val)
