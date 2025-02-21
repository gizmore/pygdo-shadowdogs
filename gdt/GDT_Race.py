from gdo.core.GDT_Enum import GDT_Enum


class GDT_Race(GDT_Enum):

    _npcs: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._npcs = False

    def npcs(self, npcs: bool=True):
        self._npcs = npcs
        return self

    def gdo_choices(self) -> dict:
        if self._npcs:
            return {
                'dragon': 'Dragon',
                'elve': 'Elve',
                'human': 'Human',
                'animal': 'Animal',
                'ork': 'Ork',
            }
        return {
            'elve': 'Elve',
            'human': 'Human',
            'ork': 'Ork',
        }
