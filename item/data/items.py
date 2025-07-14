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

        'TinfoilCap': {'klass': 'Helmet', 'level': 0, 'et': 36, 'weight': 283, 'defense': 2, 'marm': 1, 'farm': 1, 'price': 489.8},
        'DuctTapeHood': {'klass': 'Helmet', 'level': 1, 'et': 53, 'weight': 243, 'defense': 2, 'marm': 0, 'farm': 2, 'price': 521.01},
        'BaseballCap': {'klass': 'Helmet', 'level': 2, 'et': 47, 'weight': 349, 'defense': 1, 'marm': 0, 'farm': 1, 'price': 464.0},
        'SkiMask': {'klass': 'Helmet', 'level': 3, 'et': 43, 'weight': 193, 'defense': 2, 'marm': 1, 'farm': 1, 'price': 487.3},
        'GuyFawkesMask': {'klass': 'Helmet', 'level': 4, 'et': 43, 'weight': 353, 'defense': 1, 'marm': 1, 'farm': 0, 'price': 477.73},
        'LeatherHood': {'klass': 'Helmet', 'level': 5, 'et': 56, 'weight': 395, 'defense': 2, 'marm': 1, 'farm': 1, 'price': 682.88},
        'CombatHelmet': {'klass': 'Helmet', 'level': 6, 'et': 50, 'weight': 537, 'defense': 2, 'marm': 0, 'farm': 2, 'price': 778.78},
        'GasMask': {'klass': 'Helmet', 'level': 7, 'et': 37, 'weight': 367, 'defense': 4, 'marm': 1, 'farm': 3, 'price': 907.92},
        'RiotHelmet': {'klass': 'Helmet', 'level': 8, 'et': 63, 'weight': 513, 'defense': 4, 'marm': 2, 'farm': 2, 'price': 1110.36},
        'VisorHelmet': {'klass': 'Helmet', 'level': 9, 'et': 51, 'weight': 523, 'defense': 3, 'marm': 1, 'farm': 2, 'price': 963.22},
        'DigitalHalo': {'klass': 'Helmet', 'level': 10, 'et': 68, 'weight': 601, 'defense': 4, 'marm': 3, 'farm': 1, 'price': 1238.25},
        'QuantumVisor': {'klass': 'Helmet', 'level': 11, 'et': 66, 'weight': 634, 'defense': 5, 'marm': 3, 'farm': 2, 'price': 1428.51},
        'Balaclava': {'klass': 'Helmet', 'level': 12, 'et': 64, 'weight': 428, 'defense': 5, 'marm': 0, 'farm': 5, 'price': 1289.34},
        'TacticalHood': {'klass': 'Helmet', 'level': 13, 'et': 70, 'weight': 816, 'defense': 5, 'marm': 0, 'farm': 5, 'price': 1642.47},
        'KevlarCap': {'klass': 'Helmet', 'level': 14, 'et': 51, 'weight': 573, 'defense': 6, 'marm': 2, 'farm': 4, 'price': 1567.76},
        'StealthDome': {'klass': 'Helmet', 'level': 15, 'et': 58, 'weight': 716, 'defense': 7, 'marm': 1, 'farm': 6, 'price': 1896.95},
        'CryoHelmet': {'klass': 'Helmet', 'level': 16, 'et': 76, 'weight': 616, 'defense': 6, 'marm': 4, 'farm': 2, 'price': 1749.44},
        'DroneMask': {'klass': 'Helmet', 'level': 17, 'et': 51, 'weight': 554, 'defense': 6, 'marm': 4, 'farm': 2, 'price': 1638.61},
        'EchoVisor': {'klass': 'Helmet', 'level': 18, 'et': 50, 'weight': 899, 'defense': 8, 'marm': 4, 'farm': 4, 'price': 2297.38},
        'FirewallHelmet': {'klass': 'Helmet', 'level': 19, 'et': 50, 'weight': 790, 'defense': 7, 'marm': 5, 'farm': 2, 'price': 2070.9},
        'ReflectiveHelm': {'klass': 'Helmet', 'level': 20, 'et': 80, 'weight': 1077, 'defense': 7, 'marm': 5, 'farm': 2, 'price': 2476.8},
        'EMPCap': {'klass': 'Helmet', 'level': 21, 'et': 77, 'weight': 853, 'defense': 8, 'marm': 5, 'farm': 3, 'price': 2477.06},
        'ServoCrown': {'klass': 'Helmet', 'level': 22, 'et': 77, 'weight': 849, 'defense': 8, 'marm': 6, 'farm': 2, 'price': 2513.95},
        'NeuroShield': {'klass': 'Helmet', 'level': 23, 'et': 76, 'weight': 1093, 'defense': 8, 'marm': 2, 'farm': 6, 'price': 2781.13},
        'HardenedSkull': {'klass': 'Helmet', 'level': 24, 'et': 65, 'weight': 1249, 'defense': 9, 'marm': 7, 'farm': 2, 'price': 3115.04},
        'PolymeshHelm': {'klass': 'Helmet', 'level': 25, 'et': 57, 'weight': 910, 'defense': 9, 'marm': 6, 'farm': 3, 'price': 2800.69},
        'BioScannerCap': {'klass': 'Helmet', 'level': 26, 'et': 85, 'weight': 919, 'defense': 8, 'marm': 2, 'farm': 6, 'price': 2778.43},
        'Shadowvisor': {'klass': 'Helmet', 'level': 27, 'et': 80, 'weight': 1131, 'defense': 9, 'marm': 4, 'farm': 5, 'price': 3205.28},
        'MechHelm': {'klass': 'Helmet', 'level': 28, 'et': 80, 'weight': 864, 'defense': 10, 'marm': 8, 'farm': 2, 'price': 3176.28},
        'OblivionCrown': {'klass': 'Helmet', 'level': 29, 'et': 80, 'weight': 972, 'defense': 11, 'marm': 5, 'farm': 6, 'price': 3533.14},
        'NovaCrest': {'klass': 'Helmet', 'level': 30, 'et': 64, 'weight': 1267, 'defense': 12, 'marm': 1, 'farm': 11, 'price': 4025.35},

        'TShirt':        {'klass': 'Armor', 'level': 0, 'et': 40, 'weight':  250, 'marm': 0, 'farm': 0},
        'Clothes':       {'klass': 'Armor', 'level': 0, 'et': 50, 'weight':  750, 'marm': 1, 'farm': 0},
        'Jacket':        {'klass': 'Armor', 'level': 0, 'et': 60, 'weight': 1250, 'marm': 1, 'farm': 1},
        'KevlarVest':    {'klass': 'Armor', 'level': 3, 'et': 60, 'weight': 2000, 'marm': 3, 'farm': 1},
        'TacticalVest':  {'klass': 'Armor', 'level': 5, 'et': 65, 'weight': 2500, 'marm': 4, 'farm': 2},
        'NanoFiberSuit': {'klass': 'Armor', 'level': 8, 'et': 70, 'weight': 1800, 'marm': 5, 'farm': 3},

        'Trousers':       {'klass': 'Trousers', 'level': 0, 'et': 50, 'weight': 600,  'defense': 1, 'marm': 1, 'farm': 0},
        'Jeans':          {'klass': 'Trousers', 'level': 1, 'et': 55, 'weight': 800,  'defense': 1, 'marm': 1, 'farm': 1},
        'KevlarLeggings': {'klass': 'Trousers', 'level': 5, 'et': 60, 'weight': 1400, 'defense': 2, 'marm': 3, 'farm': 1},

        'Sandals': {'klass': 'Boots', 'level': 0, 'et': 45, 'weight': 183, 'defense': 0, 'marm': 1, 'farm': 0, 'price': 327.3},
        'RagShoes': {'klass': 'Boots', 'level': 1, 'et': 31, 'weight': 167, 'defense': 1, 'marm': 0, 'farm': 1, 'price': 288.98},
        'WoolSlippers': {'klass': 'Boots', 'level': 2, 'et': 38, 'weight': 165, 'defense': 1, 'marm': 1, 'farm': 0, 'price': 312.29},
        'Sneakers': {'klass': 'Boots', 'level': 3, 'et': 37, 'weight': 215, 'defense': 2, 'marm': 1, 'farm': 1, 'price': 460.27},
        'SteelToes': {'klass': 'Boots', 'level': 4, 'et': 39, 'weight': 194, 'defense': 3, 'marm': 2, 'farm': 1, 'price': 575.91},
        'CombatBoots': {'klass': 'Boots', 'level': 5, 'et': 55, 'weight': 382, 'defense': 1, 'marm': 0, 'farm': 1, 'price': 524.11},
        'TacticalWalkers': {'klass': 'Boots', 'level': 6, 'et': 35, 'weight': 201, 'defense': 4, 'marm': 3, 'farm': 1, 'price': 711.85},
        'ThermalTreads': {'klass': 'Boots', 'level': 7, 'et': 46, 'weight': 419, 'defense': 4, 'marm': 1, 'farm': 3, 'price': 908.73},
        'SilentSteps': {'klass': 'Boots', 'level': 8, 'et': 50, 'weight': 477, 'defense': 4, 'marm': 4, 'farm': 0, 'price': 978.97},
        'UrbanGrips': {'klass': 'Boots', 'level': 9, 'et': 58, 'weight': 318, 'defense': 3, 'marm': 3, 'farm': 0, 'price': 780.96},
        'NomadBoots': {'klass': 'Boots', 'level': 10, 'et': 36, 'weight': 292, 'defense': 4, 'marm': 4, 'farm': 0, 'price': 837.47},
        'AnkleGuards': {'klass': 'Boots', 'level': 11, 'et': 47, 'weight': 529, 'defense': 4, 'marm': 3, 'farm': 1, 'price': 1063.88},
        'RunnerBoots': {'klass': 'Boots', 'level': 12, 'et': 55, 'weight': 373, 'defense': 4, 'marm': 3, 'farm': 1, 'price': 989.65},
        'PaddedStompers': {'klass': 'Boots', 'level': 13, 'et': 52, 'weight': 360, 'defense': 4, 'marm': 1, 'farm': 3, 'price': 987.29},
        'GravBoots': {'klass': 'Boots', 'level': 14, 'et': 61, 'weight': 515, 'defense': 4, 'marm': 4, 'farm': 0, 'price': 1155.74},
        'ReinforcedHeels': {'klass': 'Boots', 'level': 15, 'et': 68, 'weight': 526, 'defense': 5, 'marm': 2, 'farm': 3, 'price': 1347.47},
        'SpiderClimbers': {'klass': 'Boots', 'level': 16, 'et': 58, 'weight': 796, 'defense': 6, 'marm': 6, 'farm': 0, 'price': 1697.97},
        'ShockAbsorbers': {'klass': 'Boots', 'level': 17, 'et': 42, 'weight': 597, 'defense': 5, 'marm': 0, 'farm': 5, 'price': 1361.52},
        'MagStep': {'klass': 'Boots', 'level': 18, 'et': 65, 'weight': 784, 'defense': 7, 'marm': 3, 'farm': 4, 'price': 1915.06},
        'VoidWalkers': {'klass': 'Boots', 'level': 19, 'et': 73, 'weight': 551, 'defense': 8, 'marm': 0, 'farm': 8, 'price': 1924.41},
        'StealthSoles': {'klass': 'Boots', 'level': 20, 'et': 63, 'weight': 624, 'defense': 6, 'marm': 2, 'farm': 4, 'price': 1678.3},
        'RiotBoots': {'klass': 'Boots', 'level': 21, 'et': 76, 'weight': 678, 'defense': 7, 'marm': 2, 'farm': 5, 'price': 1953.31},
        'BlastGuards': {'klass': 'Boots', 'level': 22, 'et': 74, 'weight': 835, 'defense': 7, 'marm': 3, 'farm': 4, 'price': 2115.71},
        'HazmatTreads': {'klass': 'Boots', 'level': 23, 'et': 52, 'weight': 560, 'defense': 7, 'marm': 1, 'farm': 6, 'price': 1814.84},
        'ServoWalkers': {'klass': 'Boots', 'level': 24, 'et': 56, 'weight': 858, 'defense': 10, 'marm': 5, 'farm': 5, 'price': 2614.03},
        'AntiGravFeet': {'klass': 'Boots', 'level': 25, 'et': 78, 'weight': 814, 'defense': 8, 'marm': 1, 'farm': 7, 'price': 2369.73},
        'PhaseBoots': {'klass': 'Boots', 'level': 26, 'et': 64, 'weight': 924, 'defense': 10, 'marm': 4, 'farm': 6, 'price': 2783.83},
        'NightStalkers': {'klass': 'Boots', 'level': 27, 'et': 72, 'weight': 779, 'defense': 10, 'marm': 8, 'farm': 2, 'price': 2715.84},
        'TitanGreaves': {'klass': 'Boots', 'level': 28, 'et': 75, 'weight': 1187, 'defense': 11, 'marm': 6, 'farm': 5, 'price': 3333.18},
        'WardenTreads': {'klass': 'Boots', 'level': 29, 'et': 80, 'weight': 955, 'defense': 10, 'marm': 6, 'farm': 4, 'price': 2997.82},
        'OblivionStriders': {'klass': 'Boots', 'level': 30, 'et': 75, 'weight': 882, 'defense': 10, 'marm': 2, 'farm': 8, 'price': 2944.5},

        'FingerlessGloves': {'klass': 'Gloves', 'level': 1, 'et': 37, 'weight': 81, 'defense': 1, 'marm': 0, 'farm': 0, 'price': 232.56},
        'Gloves': {'klass': 'Gloves', 'level': 0, 'et': 47, 'weight': 135, 'defense': 1, 'marm': 1, 'farm': 1, 'price': 280.0},
        'WoolGloves': {'klass': 'Gloves', 'level': 2, 'et': 38, 'weight': 162, 'defense': 1, 'marm': 1, 'farm': 0, 'price': 281.84},
        'WorkGloves': {'klass': 'Gloves', 'level': 3, 'et': 52, 'weight': 125, 'defense': 2, 'marm': 1, 'farm': 1, 'price': 405.45},
        'GripMitts': {'klass': 'Gloves', 'level': 4, 'et': 45, 'weight': 241, 'defense': 2, 'marm': 2, 'farm': 0, 'price': 456.84},
        'PaddedGloves': {'klass': 'Gloves', 'level': 5, 'et': 36, 'weight': 249, 'defense': 3, 'marm': 2, 'farm': 1, 'price': 549.45},
        'CombatGloves': {'klass': 'Gloves', 'level': 6, 'et': 26, 'weight': 152, 'defense': 4, 'marm': 0, 'farm': 4, 'price': 583.52},
        'TacticalGrips': {'klass': 'Gloves', 'level': 7, 'et': 33, 'weight': 202, 'defense': 3, 'marm': 1, 'farm': 2, 'price': 534.09},
        'LeatherWraps': {'klass': 'Gloves', 'level': 8, 'et': 42, 'weight': 330, 'defense': 2, 'marm': 1, 'farm': 1, 'price': 533.6},
        'KnucklePads': {'klass': 'Gloves', 'level': 9, 'et': 32, 'weight': 303, 'defense': 5, 'marm': 4, 'farm': 1, 'price': 833.67},
        'ShockGloves': {'klass': 'Gloves', 'level': 10, 'et': 59, 'weight': 249, 'defense': 5, 'marm': 0, 'farm': 5, 'price': 896.4},
        'FrictionSkins': {'klass': 'Gloves', 'level': 11, 'et': 53, 'weight': 419, 'defense': 5, 'marm': 5, 'farm': 0, 'price': 996.74},
        'ThermalMitts': {'klass': 'Gloves', 'level': 12, 'et': 56, 'weight': 263, 'defense': 6, 'marm': 4, 'farm': 2, 'price': 1043.46},
        'CarbonKnuckles': {'klass': 'Gloves', 'level': 13, 'et': 62, 'weight': 352, 'defense': 5, 'marm': 1, 'farm': 4, 'price': 1015.56},
        'ArmorWeaveGloves': {'klass': 'Gloves', 'level': 14, 'et': 64, 'weight': 341, 'defense': 6, 'marm': 5, 'farm': 1, 'price': 1152.64},
        'ServoFingers': {'klass': 'Gloves', 'level': 15, 'et': 59, 'weight': 500, 'defense': 6, 'marm': 5, 'farm': 1, 'price': 1257.75},
        'AntiSlashGloves': {'klass': 'Gloves', 'level': 16, 'et': 50, 'weight': 353, 'defense': 7, 'marm': 0, 'farm': 7, 'price': 1275.78},
        'SparkGuards': {'klass': 'Gloves', 'level': 17, 'et': 66, 'weight': 572, 'defense': 5, 'marm': 3, 'farm': 2, 'price': 1240.84},
        'ClimbClaws': {'klass': 'Gloves', 'level': 18, 'et': 42, 'weight': 533, 'defense': 6, 'marm': 1, 'farm': 5, 'price': 1280.44},
        'MagGripGloves': {'klass': 'Gloves', 'level': 19, 'et': 54, 'weight': 581, 'defense': 6, 'marm': 4, 'farm': 2, 'price': 1373.79},
        'BioPulseGloves': {'klass': 'Gloves', 'level': 20, 'et': 49, 'weight': 392, 'defense': 7, 'marm': 1, 'farm': 6, 'price': 1376.9},
        'CryoGraspers': {'klass': 'Gloves', 'level': 21, 'et': 47, 'weight': 580, 'defense': 9, 'marm': 9, 'farm': 0, 'price': 1792.75},
        'HazmatGloves': {'klass': 'Gloves', 'level': 22, 'et': 49, 'weight': 512, 'defense': 9, 'marm': 1, 'farm': 8, 'price': 1776.24},
        'StealthGrips': {'klass': 'Gloves', 'level': 23, 'et': 56, 'weight': 597, 'defense': 9, 'marm': 8, 'farm': 1, 'price': 1888.51},
        'NeuroTouchGloves': {'klass': 'Gloves', 'level': 24, 'et': 69, 'weight': 713, 'defense': 9, 'marm': 3, 'farm': 6, 'price': 2048.32},
        'PhaseGrips': {'klass': 'Gloves', 'level': 25, 'et': 58, 'weight': 720, 'defense': 8, 'marm': 3, 'farm': 5, 'price': 1897.5},
        'GauntletMK1': {'klass': 'Gloves', 'level': 26, 'et': 63, 'weight': 710, 'defense': 9, 'marm': 4, 'farm': 5, 'price': 2078.6},
        'TitanHands': {'klass': 'Gloves', 'level': 27, 'et': 73, 'weight': 521, 'defense': 10, 'marm': 3, 'farm': 7, 'price': 2145.22},
        'GravPalms': {'klass': 'Gloves', 'level': 28, 'et': 62, 'weight': 820, 'defense': 9, 'marm': 5, 'farm': 4, 'price': 2215.2},
        'WardenGloves': {'klass': 'Gloves', 'level': 29, 'et': 53, 'weight': 514, 'defense': 11, 'marm': 1, 'farm': 10, 'price': 2266.51},
        'OblivionClaws': {'klass': 'Gloves', 'level': 30, 'et': 79, 'weight': 636, 'defense': 10, 'marm': 9, 'farm': 1, 'price': 2344.8},

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

        'Medkit':      {'klass': 'Usable', 'level': 2, 'weight': 500},
        'Stimulant':   {'klass': 'Usable', 'level': 3, 'weight': 200},

        'Coke':        {'klass': 'Consumable', 'level': 1, 'weight': 400},
        'EnergyDrink': {'klass': 'Consumable', 'level': 1, 'weight': 300},

        'Ammo7mm':      {'klass': 'Ammo', 'level': 2, 'at': 25, 'et': 15, 'rng': 4, 'weight': 25, 'attack': 7, 'defense': 1, 'min_dmg': 3, 'max_dmg': 8},
        'Ammo8mm':      {'klass': 'Ammo', 'level': 2, 'at': 25, 'et': 15, 'rng': 4, 'weight': 40, 'attack': 7, 'defense': 1, 'min_dmg': 3, 'max_dmg': 8},
        'Ammo9mm':      {'klass': 'Ammo', 'level': 3, 'weight': 55},
        'Ammo12Gauge':  {'klass': 'Ammo', 'level': 5, 'weight': 500},
        'Ammo13':       {'klass': 'Ammo', 'level': 7, 'weight': 110},

        'CyberEye':    {'klass': 'Implant', 'level': 6, 'weight': 100, 'marm': 0, 'farm': 0},
        'NeuralLink':  {'klass': 'Implant', 'level': 8, 'weight': 80, 'marm': 0, 'farm': 0},

        'RhinoDeck':   {'klass': 'Deck', 'level': 1,  'weight': 500, 'mcpu': 6},
        'UserDeck':    {'klass': 'Deck', 'level': 5,  'weight': 600, 'mcpu': 9},
        'ControlDeck': {'klass': 'Deck', 'level': 8,  'weight': 1200, 'mcpu': 50},
        'HackingDeck': {'klass': 'Deck', 'level': 16, 'weight': 700, 'mcpu': 30, 'hac': 4},
        'MetaDeck':    {'klass': 'Deck', 'level': 24, 'weight': 700, 'mcpu': 50, 'hac': 5},

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

        'EmailArmy':   {'klass': 'Email', 'key': 'sd_email_army'},
        'NoteGizmore': {'klass': 'Note',  'key': 'sd_note_gizmore'},
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
