from gdo.shadowdogs.npcs.HardMob import HardMob
from gdo.shadowdogs.npcs.Mob import Mob
from gdo.shadowdogs.npcs.Police import Police


class npcs:

    NPCS = {
        'reaper':   {'klass': Mob,    'p_level': 999, 'p_max_hp': (100, 100)},
        'police':   {'klass': Police, 'eq': ['SteelToes', 'KevlarVest', '9mm Pistol', 'KevlarLeggings']},

        'lamer':    {'klass': Mob,     'p_level': 1,                  'p_max_hp': (1, 2), 'eq': ['Trousers', 'TShirt']},
        'haider':   {'klass': Mob,     'p_level': 2,                  'p_max_hp': (1, 3), 'eq': ['Sandals', 'Trousers', 'TShirt']},
        'noob':     {'klass': Mob,     'p_level': 3,                  'p_max_hp': (2, 3), 'eq': ['RagShoes', 'Trousers', 'Jacket']},
        'robber':   {'klass': Mob,     'p_level': 4,                  'p_max_hp': (2, 4), 'eq': ['RagShoes', 'Trousers', 'Jacket']},
        'gangster': {'klass': Mob,     'p_level': 5,                  'p_max_hp': (3, 4), 'eq': ['Shoes', 'Trousers', 'Pullover', 'Bytegun']},
        'goblin':   {'klass': Mob,     'p_level': 6, 'p_race': 'ork', 'p_max_hp': (3, 5), 'eq': ['Shoes', 'Trousers', 'Pullover', 'Bytegun']},
        'ork':      {'klass': HardMob, 'p_level': 8, 'p_race': 'ork', 'p_max_hp': (4, 6), 'eq': ['CombatBoots', 'Jeans', 'LeatherVest', 'Sword']},
    }

    CLASSES = {
        Mob.__name__: Mob,
        HardMob.__name__: HardMob,
        Police.__name__: Police,
    }

    @classmethod
    def get_class(cls, klass: str):
        return cls.CLASSES.get(klass, Mob)
