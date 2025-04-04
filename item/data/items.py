import glob
import importlib
import inspect
import os

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.item.Item import Item


class items:

    KLASSES = {}

    ITEMS = {
        'Fists':        {'klass': 'Fists',  'wei': 0,  'atk': 4, 'dmg': [2, 5]},
        'Knuckles':     {'klass': 'Melee',  'wei': 0,  'atk': 4, 'dmg': [2, 6]},
        'Club':         {'klass': 'Thrust', 'wei': 0, 'atk': 4, 'dmg': [2, 6]},
        'ShortSword':   {'klass': 'Sword',  'wei': 0,  'atk': 6, 'dmg': []},
        'Sword':        {'klass': 'Sword',  'wei': 0,  'atk': 6, 'dmg': []},
        'LongSword':    {'klass': 'Sword',  'wei': 0, 'atk': 6, 'dmg': []},
        'SmallAxe':     {'klass': 'Thrust', 'wei': 0, 'atk': 6, 'dmg': []},
        'MorningStar':  {'klass': 'Thrust', 'wei': 0, 'atk': 6, 'dmg': []},

        'Jeans':        {'klass': 'Trousers', 'wei': 0, },

        'Sandals':      {'klass': 'Boots',  'wei': 0,  'def': 1, 'arm': 1},
        'Shoes':        {'klass': 'Boots',  'wei': 0,  'def': 2, 'arm': 1},
        'Boots':        {'klass': 'Boots',  'wei': 0,  'def': 2, 'arm': 2},
        'LeatherBoots': {'klass': 'Boots',  'wei': 0,  'def': 2, 'arm': 2},

        'Ring':         {'klass': 'Ring', },
        'WeddingRing':  {'klass': 'WeddingRing', 'wei': 25, },

        'Pen':          {'klass': 'Pen', 'wei': 20}
    }

    @classmethod
    def load(cls):
        if len(cls.KLASSES):
            return
        from gdo.shadowdogs.item.Item import Item
        items_path = f"gdo/shadowdogs/item/classes"
        item_files = glob.glob(f"{items_path}/*.py")
        for file_path in item_files:
            filename = os.path.basename(file_path)
            if "/_" in filename:
                continue
            module_name = file_path.replace("/", ".").replace("\\", ".")
            module_name = os.path.splitext(module_name)[0]
            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, Item):
                        cls.KLASSES[name] = obj
            except Exception as e:
                print(f"Failed to load {module_name}: {e}")
    @classmethod
    def instance(cls, klass: str) -> 'Item':
        return cls.KLASSES[klass]()

    @classmethod
    def get_item(cls, name: str, count: int, mods: dict[str,int]):
        data = cls.ITEMS[name]
        item = cls.instance(data['klass']).count(count).modifiers(mods)

        pass
