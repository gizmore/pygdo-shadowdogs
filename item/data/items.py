import glob
import importlib.util
import inspect
import os

from typing import TYPE_CHECKING

from gdo.base.Application import Application
from gdo.base.Logger import Logger
from gdo.base.Util import Strings

if TYPE_CHECKING:
    from gdo.shadowdogs.item.Item import Item


class items:

    KLASSES = {}
    ITEMS = {
        'Fists'  :         {'klass': 'Fists',  'level': 0, 'at': 30, 'et':  1, 'rng': 1, 'weight': 0,    'attack': 4, 'defense': 1, 'min_dmg': 1, 'max_dmg': 4},
        'BronzeKnuckles':  {'klass': 'Fists',  'level': 1, 'at': 30, 'et': 30, 'rng': 1,  'weight': 500,  'attack': 4, 'defense': 2, 'min_dmg': 2, 'max_dmg': 6},
        'SteelKnuckles':   {'klass': 'Fists',  'level': 1, 'at': 30, 'et': 30, 'rng': 1,  'weight': 600,  'attack': 4, 'defense': 2, 'min_dmg': 3, 'max_dmg': 6},
        'Club':            {'klass': 'Thrust', 'level': 2, 'at': 30, 'et': 30, 'rng': 1,  'weight': 1500, 'attack': 4, 'defense': 1, 'min_dmg': 2, 'max_dmg': 6},
        'ShortSword':      {'klass': 'Sword',  'level': 3, 'at': 30, 'et': 30, 'rng': 2,  'weight': 1200, 'attack': 6, 'defense': 2, 'min_dmg': 3, 'max_dmg': 8},
        'Sword':           {'klass': 'Sword',  'level': 3, 'at': 30, 'et': 30, 'rng': 2, 'weight': 1500, 'attack': 6, 'defense': 2, 'min_dmg': 4, 'max_dmg': 10},
        'LongSword':       {'klass': 'Sword',  'level': 5, 'at': 30, 'et': 30, 'rng': 2,  'weight': 1800, 'attack': 6, 'defense': 2, 'min_dmg': 4, 'max_dmg': 12},
        'SmallAxe':        {'klass': 'Thrust', 'level': 5, 'at': 30, 'et': 30, 'rng': 2,  'weight': 1000, 'attack': 6, 'defense': 1, 'min_dmg': 5, 'max_dmg': 9},
        'MorningStar':     {'klass': 'Thrust', 'level': 5, 'at': 30, 'et': 30, 'rng': 2,  'weight': 2500, 'attack': 6, 'defense': 0, 'min_dmg': 5, 'max_dmg': 10},

        'TinfoilCap':    {'klass': 'Helmet', 'level': 0, 'et': 30, 'weight': 100, 'defense': 1, 'marm': 0, 'farm': 1},
        'BaseballCap':   {'klass': 'Helmet', 'level': 1, 'et': 30, 'weight': 180, 'defense': 1, 'marm': 1, 'farm': 1},
        'GuyFawkesMask': {'klass': 'Helmet', 'level': 1, 'et': 40, 'weight': 400, 'defense': 0, 'marm': 2, 'farm': 0},

        'TShirt':       {'klass': 'Armor', 'level': 0, 'et': 40, 'weight':  250, 'marm': 0, 'farm': 0},
        'Clothes':      {'klass': 'Armor', 'level': 0, 'et': 50, 'weight':  750, 'marm': 1, 'farm': 0},
        'Jacket':       {'klass': 'Armor', 'level': 0, 'et': 60, 'weight': 1250, 'marm': 1, 'farm': 1},

        'Trousers':     {'klass': 'Trousers', 'level': 0, 'et': 50, 'weight': 600, 'defense': 1, 'marm': 1, 'farm': 0},
        'Jeans':        {'klass': 'Trousers', 'level': 1, 'et': 55, 'weight': 800, 'defense': 1, 'marm': 1, 'farm': 1},

        'Sandals':      {'klass': 'Boots', 'level': 0, 'et': 30, 'weight': 300,  'defense': 1, 'marm': 1},
        'Shoes':        {'klass': 'Boots', 'level': 1, 'et': 30, 'weight': 900,  'defense': 2, 'marm': 1},
        'Boots':        {'klass': 'Boots', 'level': 1, 'et': 30, 'weight': 1200, 'defense': 2, 'marm': 2},
        'LeatherBoots': {'klass': 'Boots', 'level': 1, 'et': 30, 'weight': 1600, 'defense': 2, 'marm': 2},

        'Ring':         {'klass': 'Ring', 'level': 6, 'weight': 10},
        'WeddingRing':  {'klass': 'WeddingRing', 'level': 20, 'weight': 25},

        'Pen':          {'klass': 'Pen', 'weight': 20},
        'MobilePhone':  {'klass': 'MobilePhone', 'weight': 488},
    }

    @classmethod
    def load(cls):
        if cls.KLASSES:
            return
        from gdo.shadowdogs.item.Item import Item
        items_path = Application.file_path("gdo/shadowdogs/item/classes")
        item_files = glob.glob(f"{items_path}/**/*.py", recursive=True)
        for file_path in item_files:
            if "/_" in file_path:
                continue
            module_name = 'gdo/' + Strings.substr_from(file_path, '/gdo/')
            module_name = module_name.replace("/", ".")
            module_name = os.path.splitext(module_name)[0]
            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, Item):
                        cls.KLASSES[name] = obj
            except Exception as e:
                Logger.exception(e)

    @classmethod
    def instance(cls, name: str, klass: str) -> 'Item':
        return cls.KLASSES[klass](name)

    @classmethod
    def get_item(cls, name: str, count: int = 1, mods: str | None = None):
        data = cls.ITEMS[name]
        return cls.instance(name, data['klass']).count(count).modifiers(mods)
