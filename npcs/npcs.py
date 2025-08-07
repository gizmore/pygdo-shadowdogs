from gdo.shadowdogs.npcs.Peine.Lazer import Lazer
from gdo.shadowdogs.npcs.Mob import Mob
from gdo.shadowdogs.npcs.Peine.Mom import Mom


class npcs:

    NPCS = {
        'reaper':   {'klass': Mob, 'level': 999, 'max_hp': (100, 100)},
        'lazer':    {'klass': Lazer, 'level': 3},
        'mom':      {'klass': Mom, 'level': 2},
        'lamer':    {'klass': Mob, 'level': 1, 'max_hp': (1,3), 'eq': ['Sandals', 'Trousers', 'TShirt']},
        'haider':     {'klass': Mob, 'level': 2, 'max_hp': (2,5), 'eq': ['Shoes', 'Trousers', 'TShirt']},
        'noob':     {'klass': Mob, 'level': 3, 'max_hp': (3,6), 'eq': ['Boots', 'Trousers', 'Jacket']},
        'gangster': {'klass': Mob, 'level': 4, 'max_hp': (4,6), 'eq': ['Shoes', 'Trousers', 'Pullover', 'Bytegun']},
    }
