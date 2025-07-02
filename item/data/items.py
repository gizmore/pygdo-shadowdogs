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
        'Fists':          {'klass': 'Fists', 'level': 0, 'at': 30, 'et': 1, 'rng': 1, 'weight': 0, 'attack': 4, 'defense': 1, 'min_dmg': 1, 'max_dmg': 4, 'eur': 0},
        'BronzeKnuckles': {'klass': 'Fists', 'level': 1, 'at': 30, 'et': 30, 'rng': 1, 'weight': 500, 'attack': 4, 'defense': 2, 'min_dmg': 2, 'max_dmg': 6, 'eur': 50},
        'SteelKnuckles':  {'klass': 'Fists', 'level': 1, 'at': 30, 'et': 30, 'rng': 1, 'weight': 600, 'attack': 4, 'defense': 2, 'min_dmg': 3, 'max_dmg': 6, 'eur': 75},
        'Club':           {'klass': 'Thrust', 'level': 2, 'at': 30, 'et': 30, 'rng': 1, 'weight': 1500, 'attack': 4, 'defense': 1, 'min_dmg': 2, 'max_dmg': 6, 'eur': 80},
        'ShortSword':     {'klass': 'Sword', 'level': 3, 'at': 30, 'et': 30, 'rng': 2, 'weight': 1200, 'attack': 6, 'defense': 2, 'min_dmg': 3, 'max_dmg': 8, 'eur': 150},
        'Sword':          {'klass': 'Sword', 'level': 3, 'at': 30, 'et': 30, 'rng': 2, 'weight': 1500, 'attack': 6, 'defense': 2, 'min_dmg': 4, 'max_dmg': 10, 'eur': 180},
        'LongSword':      {'klass': 'Sword', 'level': 5, 'at': 30, 'et': 30, 'rng': 2, 'weight': 1800, 'attack': 6, 'defense': 2, 'min_dmg': 4, 'max_dmg': 12, 'eur': 250},
        'SmallAxe':       {'klass': 'Thrust', 'level': 5, 'at': 30, 'et': 30, 'rng': 2, 'weight': 1000, 'attack': 6, 'defense': 1, 'min_dmg': 5, 'max_dmg': 9, 'eur': 220},
        'MorningStar':    {'klass': 'Thrust', 'level': 5, 'at': 30, 'et': 30, 'rng': 2, 'weight': 2500, 'attack': 6, 'defense': 0, 'min_dmg': 5, 'max_dmg': 10, 'eur': 260},
        'Machete':        {'klass': 'Sword', 'level': 4, 'at': 30, 'et': 30, 'rng': 2, 'weight': 1600, 'attack': 7, 'defense': 2, 'min_dmg': 4, 'max_dmg': 10, 'eur': 240},
        'Katana':         {'klass': 'Sword', 'level': 6, 'at': 28, 'et': 25, 'rng': 2, 'weight': 1400, 'attack': 8, 'defense': 3, 'min_dmg': 6, 'max_dmg': 12, 'eur': 400},
        'Chainsword':     {'klass': 'Sword', 'level': 8, 'at': 35, 'et': 35, 'rng': 2, 'weight': 2200, 'attack': 10, 'defense': 2, 'min_dmg': 8, 'max_dmg': 16, 'eur': 600},
        'Crowbar':        {'klass': 'Thrust', 'level': 2, 'at': 25, 'et': 20, 'rng': 1, 'weight': 1800, 'attack': 5, 'defense': 2, 'min_dmg': 3, 'max_dmg': 8, 'eur': 120},

        'TinfoilCap':    {'klass': 'Helmet', 'level': 0, 'et': 30, 'weight': 100,  'defense': 1, 'marm': 0, 'farm': 1},
        'BaseballCap':   {'klass': 'Helmet', 'level': 1, 'et': 30, 'weight': 180,  'defense': 1, 'marm': 1, 'farm': 1},
        'GuyFawkesMask': {'klass': 'Helmet', 'level': 1, 'et': 40, 'weight': 400,  'defense': 0, 'marm': 2, 'farm': 0},
        'CombatHelmet':  {'klass': 'Helmet', 'level': 3, 'et': 45, 'weight': 900,  'defense': 2, 'marm': 3, 'farm': 1},
        'VisorHelmet':   {'klass': 'Helmet', 'level': 6, 'et': 50, 'weight': 1100, 'defense': 3, 'marm': 4, 'farm': 2},

        'TShirt':        {'klass': 'Armor', 'level': 0, 'et': 40, 'weight':  250, 'marm': 0, 'farm': 0},
        'Clothes':       {'klass': 'Armor', 'level': 0, 'et': 50, 'weight':  750, 'marm': 1, 'farm': 0},
        'Jacket':        {'klass': 'Armor', 'level': 0, 'et': 60, 'weight': 1250, 'marm': 1, 'farm': 1},
        'KevlarVest':    {'klass': 'Armor', 'level': 3, 'et': 60, 'weight': 2000, 'marm': 3, 'farm': 1},
        'TacticalVest':  {'klass': 'Armor', 'level': 5, 'et': 65, 'weight': 2500, 'marm': 4, 'farm': 2},
        'NanoFiberSuit': {'klass': 'Armor', 'level': 8, 'et': 70, 'weight': 1800, 'marm': 5, 'farm': 3},

        'Trousers':       {'klass': 'Trousers', 'level': 0, 'et': 50, 'weight': 600,  'defense': 1, 'marm': 1, 'farm': 0},
        'Jeans':          {'klass': 'Trousers', 'level': 1, 'et': 55, 'weight': 800,  'defense': 1, 'marm': 1, 'farm': 1},
        'KevlarLeggings': {'klass': 'Trousers', 'level': 5, 'et': 60, 'weight': 1400, 'defense': 2, 'marm': 3, 'farm': 1},

        'Sandals':      {'klass': 'Boots', 'level': 0, 'et': 30, 'weight': 300,  'defense': 1, 'marm': 1},
        'Shoes':        {'klass': 'Boots', 'level': 1, 'et': 30, 'weight': 900,  'defense': 2, 'marm': 1},
        'Boots':        {'klass': 'Boots', 'level': 1, 'et': 30, 'weight': 1200, 'defense': 2, 'marm': 2},
        'LeatherBoots': {'klass': 'Boots', 'level': 1, 'et': 30, 'weight': 1600, 'defense': 2, 'marm': 2},
        'CombatBoots':  {'klass': 'Boots', 'level': 4, 'et': 35, 'weight': 1500, 'defense': 3, 'marm': 2},
        'NanoBoots':    {'klass': 'Boots', 'level': 7, 'et': 40, 'weight': 1000, 'defense': 4, 'marm': 3},

        'Ring':         {'klass': 'Ring',        'level': 3,  'weight': 10, 'marm': 1},
        'RingOfTruth':  {'klass': 'Ring',        'level': 12, 'weight': 12, 'max_hp': 2},
        'WeddingRing':  {'klass': 'WeddingRing', 'level': 20, 'weight': 25},

        'Pen':          {'klass': 'Pen',         'weight': 20},
        'MobilePhone':  {'klass': 'MobilePhone', 'weight': 488},

        'Bytegun':      {'klass': 'Pistol',     'level': 2, 'at': 25, 'et': 15, 'rng': 4, 'weight': 500,  'attack': 7,  'defense': 1, 'min_dmg': 3, 'max_dmg': 8},
        'StreetPistol': {'klass': 'Pistol',     'level': 3, 'at': 25, 'et': 15, 'rng': 4, 'weight': 700,  'attack': 8,  'defense': 1, 'min_dmg': 4, 'max_dmg': 10},
        'HandCannon':   {'klass': 'Pistol',     'level': 7, 'at': 20, 'et': 18, 'rng': 5, 'weight': 1300, 'attack': 11, 'defense': 0, 'min_dmg': 7, 'max_dmg': 16},
        'SMG':          {'klass': 'MachineGun', 'level': 6, 'at': 15, 'et': 12, 'rng': 6, 'weight': 1900, 'attack': 9,  'defense': 1, 'min_dmg': 5, 'max_dmg': 13},
        'Shotgun':      {'klass': 'Shotgun',    'level': 5, 'at': 20, 'et': 18, 'rng': 3, 'weight': 2500, 'attack': 12, 'defense': 1, 'min_dmg': 8, 'max_dmg': 15},

        'UserDeck':    {'klass': 'Deck', 'level': 5,  'weight': 600,  'cpu': 9},
        'ControlDeck': {'klass': 'Deck', 'level': 8,  'weight': 1200, 'cpu': 50},
        'HackingDeck': {'klass': 'Deck', 'level': 16, 'weight': 700,  'cpu': 30, 'hac': 4},
        'MetaDeck':    {'klass': 'Deck', 'level': 24, 'weight': 700, 'cpu': 50, 'hac': 5},

        'CyberEye':    {'klass': 'Implant', 'level': 6, 'weight': 100, 'marm': 0, 'farm': 0},
        'NeuralLink':  {'klass': 'Implant', 'level': 8, 'weight': 80, 'marm': 0, 'farm': 0},

        'Medkit':      {'klass': 'Usable', 'level': 2, 'weight': 500},
        'Stimulant':   {'klass': 'Usable', 'level': 3, 'weight': 200},

        'Coke':        {'klass': 'Consumable', 'level': 1, 'weight': 400},
        'EnergyDrink': {'klass': 'Consumable', 'level': 1, 'weight': 300},

        'Ammo7mm':      {'klass': 'Ammo', 'level': 2, 'at': 25, 'et': 15, 'rng': 4, 'weight': 25, 'attack': 7, 'defense': 1, 'min_dmg': 3, 'max_dmg': 8},
        'Ammo8mm':      {'klass': 'Ammo', 'level': 2, 'at': 25, 'et': 15, 'rng': 4, 'weight': 40, 'attack': 7, 'defense': 1, 'min_dmg': 3, 'max_dmg': 8},
        'Ammo9mm':      {'klass': 'Ammo', 'level': 3, 'weight': 55},
        'Ammo12Gauge':  {'klass': 'Ammo', 'level': 5, 'weight': 500},
        'Ammo13':       {'klass': 'Ammo', 'level': 7, 'weight': 110},

        'Move.exe':     {'klass': 'Move',     'level': 1},
        'Strafe.exe':   {'klass': 'Move',     'level': 2},
        'Tree.exe':     {'klass': 'Move',     'level': 4},
        'DMA.exe':      {'klass': 'DMA',      'level': 6},
        'Ping4.exe':    {'klass': 'Ping',     'level': 1},
        'Ping6.exe':    {'klass': 'Ping',     'level': 3},
        'Backdoor.exe': {'klass': 'Backdoor', 'level': 3},
        'Rootkit.exe':  {'klass': 'Backdoor', 'level': 5},
        'Modkit.exe':   {'klass': 'Backdoor', 'level': 8},
        'hydra.exe':    {'klass': 'Hydra',    'level': 4},
        'JTR.exe':      {'klass': 'Hydra',    'level': 7},
        'NMap.exe':     {'klass': 'NMap',     'level': 7},
        'Trace.exe':    {'klass': 'Trace',    'level': 2},
        'TraceNT.exe':  {'klass': 'Trace',    'level': 4},
        'TraceNG.exe':  {'klass': 'Trace',    'level': 6},
    }

    @classmethod
    def load(cls):
        if not cls.KLASSES:
            cls.load_dir(Application.file_path("gdo/shadowdogs/item/classes"))
            cls.load_dir(Application.file_path("gdo/shadowdogs/obstacle/minigame/exe"))

    @classmethod
    def instance(cls, name: str, klass: str) -> 'Item':
        return cls.KLASSES[klass](name)

    @classmethod
    def get_item(cls, name: str, count: int = 1, mods: str | None = None):
        data = cls.ITEMS[name]
        return cls.instance(name, data['klass']).count(count).modifiers(mods)

    @classmethod
    def load_dir(cls, items_path: str):
        from gdo.shadowdogs.item.Item import Item
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
