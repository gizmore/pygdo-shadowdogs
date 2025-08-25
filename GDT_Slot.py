from gdo.base.Trans import t
from gdo.core.GDT_Enum import GDT_Enum


class GDT_Slot(GDT_Enum):

    BANK = 'bank'
    BAZAAR = 'bazaar'
    CYBERDECK = 'cyberdeck'
    CYBERWARE = 'cyberware'
    INVENTORY = 'inventory'
    MOUNT = 'mount'
    SHOP = 'shop'

    NEXUS = 'nexus' # out of phase

    SLOTS = [
        'p_weapon',
        'p_armor',
        'p_helmet',
        'p_trousers',
        'p_boots',
        'p_gloves',
        'p_amulet',
        'p_ring',
        'p_earring',
        'p_piercing',
        'p_mount',
        'p_cyberdeck',
    ]

    EQUIPMENT_SLOTS = [
        'p_weapon',
        'p_armor',
        'p_helmet',
        'p_trousers',
        'p_boots',
        'p_gloves',
        'p_amulet',
        'p_ring',
        'p_earring',
    ]

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {
            'p_weapon': 'Weapon',
            'p_armor': 'Armor',
            'p_trousers': 'Trousers',
            'p_helmet': 'Helmet',
            'p_boots': 'Boots',
            'p_gloves': 'Gloves',
            'p_amulet': 'Amulet',
            'p_ring': 'Ring',
            'p_earring': 'Earring',
            'p_piercing': 'Piercing',
            'p_mount': 'Vehicle',
            'p_cyberdeck': 'Cyberdeck',

            'bank': 'Bank',
            'bazaar': 'Bazaar',
            'cyberdeck': 'Cyberdeck',
            'cyberware': 'Cyberware',
            'inventory': 'Inventory',
            'mount': 'In Vehicle',
            'shop': 'Shop',

            'nexus': 'Nexus',
        }

    @classmethod
    def map(cls, slot_name: str):
        slot_name = slot_name.lower()
        slot_name1 = slot_name[0:2]
        slot_name2 = slot_name[2:4]
        for slot in cls.SLOTS:
            chars = slot[2:4]
            if chars == slot_name1 or chars == slot_name2 or slot == slot_name:
                return slot
        return None

    @classmethod
    def display_slot(cls, slot: str):
        return t(slot)
