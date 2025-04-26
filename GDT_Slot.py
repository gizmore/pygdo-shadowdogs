from gdo.core.GDT_Enum import GDT_Enum


class GDT_Slot(GDT_Enum):

    BANK = 'bank'
    BAZAAR = 'bazaar'
    CYBERDECK = 'cyberdeck'
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

            'bank': 'Bank',
            'bazaar': 'Bazaar',
            'cyberdeck': 'Cyberdeck',
            'inventory': 'Inventory',
            'mount': 'In Vehicle',
            'shop': 'Shop',

            'nexus': 'Nexus',
        }

    @classmethod
    def map(cls, slot_name: str):
        slot_name = slot_name.lower()[0:2]
        for slot in cls.SLOTS:
            if slot[2:4] == slot_name:
                return slot
        return None
