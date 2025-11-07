from gdo.core.GDT_Enum import GDT_Enum
from typing import TYPE_CHECKING, Iterator, Tuple

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class GDT_Race(GDT_Enum):

    BASE: dict[str, dict[str, int]] = {
        'mob': {},
        'animal': {},
        'drone': {},
        'dragon': {},

        'elve':     {'p_bod': 1, 'p_mag': 2, 'p_str': 1, 'p_dex': 1, 'p_qui': 1, 'p_int': 6, 'p_wis': 2, 'p_cha': 2, 'p_luc': 1},
        'halfelve': {'p_bod': 1, 'p_mag': 1, 'p_str': 2, 'p_dex': 1, 'p_qui': 1, 'p_int': 5, 'p_wis': 1, 'p_cha': 2, 'p_luc': 1},
        'human':    {'p_bod': 1, 'p_mag': 0, 'p_str': 3, 'p_dex': 1, 'p_qui': 1, 'p_int': 4, 'p_wis': 1, 'p_cha': 1, 'p_luc': 1},
        'dwarf':    {'p_bod': 2, 'p_mag': 0, 'p_str': 4, 'p_dex': 1, 'p_qui': 0, 'p_int': 3, 'p_wis': 1, 'p_cha': 1, 'p_luc': 2},
        'halforc':  {'p_bod': 2, 'p_mag': -1, 'p_str': 5, 'p_dex': 0, 'p_qui': 0, 'p_int': 2, 'p_wis': 0, 'p_cha': 0, 'p_luc': 1},
        'orc':      {'p_bod': 2, 'p_mag': -2, 'p_str': 6, 'p_dex': 0, 'p_qui': 0, 'p_int': 1, 'p_wis': 0, 'p_cha': 0, 'p_luc': 1},
        'troll':    {'p_bod': 3, 'p_mag': -3, 'p_str': 7, 'p_dex': 0, 'p_qui': 0, 'p_int': 0, 'p_wis': 0, 'p_cha': 0, 'p_luc': 1},
    }

    BONUS: dict[str, dict[str, int]] = {
        'mob': {},
        'animal': {},
        'drone': {},
        'dragon': {},

        'elve':     {'p_dex': 1, 'p_int': 2, 'p_wis': 1, 'p_max_hp': 1, 'p_max_mp': 5, 'p_min_dmg': 0, 'p_max_dmg': 0},
        'halfelve': {'p_dex': 1, 'p_int': 1, 'p_cha': 1, 'p_mag': 1, 'p_max_hp': 1, 'p_max_mp': 2, 'p_min_dmg': 0, 'p_max_dmg': 1},
        'human':    {'p_dex': 1, 'p_wis': 1, 'p_cha': 1, 'p_luc': 1, 'p_max_hp': 2, 'p_max_mp': 1, 'p_min_dmg': 0, 'p_max_dmg': 1},
        'dwarf':    {'p_str': 2, 'p_bod': 1, 'p_wis': 1, 'p_max_hp': 2, 'p_max_mp': 1, 'p_min_dmg': 0, 'p_max_dmg': 1},
        'halforc':  {'p_str': 2, 'p_bod': 1, 'p_luc': 1, 'p_max_hp': 3, 'p_max_mp': 0, 'p_min_dmg': 1, 'p_max_dmg': 1},
        'orc':      {'p_str': 3, 'p_bod': 1, 'p_max_hp': 3, 'p_max_mp': 0, 'p_min_dmg': 1, 'p_max_dmg': 2},
        'troll':    {'p_str': 3, 'p_bod': 1, 'p_max_hp': 4, 'p_max_mp': 0, 'p_min_dmg': 2, 'p_max_dmg': 3},
    }

    GENDER: dict[str,dict[str,int]] = {
        'male':   {'p_bod': 1, 'p_str': 1},
        'female': {'p_mag': 1, 'p_int': 1, 'p_cha': 2, 'p_luc': 1},
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
        yield from bonus.items()
        bonus = self.GENDER[player.gdo_val('p_gender')]
        yield from bonus.items()

    def apply(self, player: 'SD_Player'):
        for key, val in self.all_bonuses(player):
            player.apply(key, val)
