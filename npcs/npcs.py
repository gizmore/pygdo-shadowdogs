from gdo.shadowdogs.npcs.Peine.Lazer import Lazer
from gdo.shadowdogs.npcs.Mob import Mob
from gdo.shadowdogs.npcs.Peine.Mom import Mom


class npcs:

    NPCS = {
        'reaper':   {'klass': Mob, 'level': 999, 'max_hp': (100, 100)},
        'lazer':    {'klass': Lazer, 'level': 3},
        'mom':      {'klass': Mom, 'level': 2},
        'lamer':    {'klass': Mob, 'level': 1, 'max_hp': (2,4), 'eq': ['Sandals', 'Trousers', 'TShirt']},
        'noob':     {'klass': Mob, 'level': 2, 'max_hp': (3,5), 'eq': ['Shoes', 'Trousers', 'TShirt']},
        'gangster': {'klass': Mob, 'level': 3, 'max_hp': (3,6), 'eq': ['Shoes', 'Trousers', 'Pullover']},
    }
