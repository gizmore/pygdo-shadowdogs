from gdo.shadowdogs.npcs.Mob import Mob
from gdo.shadowdogs.npcs.Police import Police


class npcs:

    NPCS = {
        'reaper':   {'klass': Mob,    'p_level': 999, 'p_max_hp': (100, 100)},
        'police':   {'klass': Police, 'eq': ['SteelToes', 'KevlarVest', '9mm Pistol', 'KevlarLeggings']},
        # 'lazer':    {'klass': Lazer, 'p_level': 3},
        # 'mom':      {'klass': Mom,   'p_level': 2},
        'lamer':    {'klass': Mob,     'p_level': 1,                  'p_max_hp': (1,3),  'eq': ['Trousers', 'TShirt']},
        'haider':   {'klass': Mob,     'p_level': 2,                  'p_max_hp': (2,5),  'eq': ['Sandals', 'Trousers', 'TShirt']},
        'noob':     {'klass': Mob,     'p_level': 3,                  'p_max_hp': (3,6),  'eq': ['RagShoes', 'Trousers', 'Jacket']},
        'robber':   {'klass': Mob,     'p_level': 4,                  'p_max_hp': (4,8),  'eq': ['RagShoes', 'Trousers', 'Jacket']},
        'gangster': {'klass': Mob,     'p_level': 5,                  'p_max_hp': (5,10), 'eq': ['Shoes', 'Trousers', 'Pullover', 'Bytegun']},
        'ork':      {'klass': Mob,     'p_level': 6, 'p_race': 'ork', 'p_max_hp': (8,12), 'eq': ['CombatBoots', 'Jeans', 'LeatherVest', 'Sword']},
    }
