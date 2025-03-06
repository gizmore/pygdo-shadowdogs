from gdo.core.GDT_Enum import GDT_Enum


class GDT_Slot(GDT_Enum):

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {
            'weapon': 'p_weapon',
            'armor': 'p_armor',
            'helmet': 'p_helmet',
            'boots': 'p_boots',
            'gloves': 'p_gloves',
            'amulet': 'p_amulet',
            'ring': 'p_ring',
        }
