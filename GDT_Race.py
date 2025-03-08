from gdo.core.GDT_Enum import GDT_Enum


class GDT_Race(GDT_Enum):

    BONUS = {
        'dragon':   {},
        'animal':   {},
        'drone':    {},

        'elve':     {'str': 1, 'int': 6, 'wis': 2},
        'halfelve': {'str': 2, 'int': 5, 'wis': 1},
        'human':    {'str': 3, 'int': 4, 'wis': 1},
        'dwarf':    {'str': 4, 'int': 3, 'wis': 1},
        'halfork':  {'str': 5, 'int': 2, 'wis': 0},
        'ork':      {'str': 6, 'int': 1, 'wis': 0},
        'troll':    {'str': 7, 'int': 0, 'wis': 0},
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
