from gdo.core.GDT_Enum import GDT_Enum


class GDT_Slot(GDT_Enum):

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {
            'p_weapon': 'Weapon',
            'p_armor': 'Armor',
            'p_helmet': 'Helmet',
            'p_boots': 'Boots',
            'p_gloves': 'Gloves',
            'p_amulet': 'Amulet',
            'p_ring': 'Ring',
            'p_piercing': 'Piercing',
            'p_mount': 'Active Mount',
            'inventory': 'Inventory',
            'mount': 'Inside Mount',
            'bank': 'bank',
        }
