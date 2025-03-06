import glob
import importlib
import inspect
import os

from gdo.shadowdogs.itembase.Item import Item


class items:
    KLASSES = {
    }

    ITEMS = {
        'Fists':        {'klass': 'Fists',  'wei': 0,  'atk': 4, 'dmg': [2, 5]},
        'Knuckles':     {'klass': 'Melee',  'wei': 0,  'atk': 4, 'dmg': [2, 6]},
        'Club':         {'klass': 'Thrust', 'wei': 0, 'atk': 4, 'dmg': [2, 6]},
        'ShortSword':   {'klass': 'Sword',  'wei': 0,  'atk': 6, 'dmg': []},
        'Sword':        {'klass': 'Sword',  'wei': 0,  'atk': 6, 'dmg': []},
        'LongSword':    {'klass': 'Sword', 'wei': 0, 'atk': 6, 'dmg': []},
        'SmallAxe':     {'klass': 'Thrust', 'wei': 0, 'atk': 6, 'dmg': []},

        'Sandals':      {'klass': 'Boots',  'def': 1, 'arm': 1},
        'Shoes':        {'klass': 'Boots',  'def': 2, 'arm': 1},
        'Boots':        {'klass': 'Boots',  'def': 2, 'arm': 2},
        'LeatherBoots': {'klass': 'Boots', 'def': 2, 'arm': 2},
    }

    @classmethod
    def load(cls):
        if len(cls.KLASSES):
            return
        items_path = f"gdo/shadowdogs/itembase"
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
                    if issubclass(obj, Item) and obj is not Item:
                        cls.KLASSES[name] = obj #.render_name()
            except Exception as e:
                print(f"Failed to load {module_name}: {e}")
