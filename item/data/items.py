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
        'Fists':           {'klass': 'Fists', 'level': 1, 'at': 60, 'et': 15, 'rng': 1, 'weight': 200, 'attack': 4, 'defense': 1, 'min_dmg': 1, 'max_dmg': 4, 'price': 50},
        'Bronze Knuckles': {'klass': 'Fists', 'level': 2, 'at': 59, 'et': 15, 'rng': 1, 'weight': 538, 'attack': 5, 'defense': 1, 'min_dmg': 2, 'max_dmg': 6, 'price': 5221},
        'Steel Knuckles':  {'klass': 'Fists', 'level': 3, 'at': 58, 'et': 15, 'rng': 1, 'weight': 876, 'attack': 5, 'defense': 1, 'min_dmg': 4, 'max_dmg': 8, 'price': 10391},
        'Club':            {'klass': 'Thrust', 'level': 4, 'at': 57, 'et': 15, 'rng': 1, 'weight': 1214, 'attack': 6, 'defense': 2, 'min_dmg': 5, 'max_dmg': 10, 'price': 15562},
        'Short Sword':     {'klass': 'Thrust', 'level': 5, 'at': 56, 'et': 15, 'rng': 1, 'weight': 1552, 'attack': 7, 'defense': 2, 'min_dmg': 6, 'max_dmg': 12, 'price': 20733},
        'Sword':           {'klass': 'Thrust', 'level': 6, 'at': 55, 'et': 15, 'rng': 1, 'weight': 1890, 'attack': 7, 'defense': 2, 'min_dmg': 8, 'max_dmg': 14, 'price': 25903},
        'Long Sword':      {'klass': 'Thrust', 'level': 7, 'at': 54, 'et': 15, 'rng': 1, 'weight': 2228, 'attack': 8, 'defense': 3, 'min_dmg': 9, 'max_dmg': 16, 'price': 31074},
        'Small Axe':       {'klass': 'Thrust', 'level': 8, 'at': 53, 'et': 15, 'rng': 1, 'weight': 2566, 'attack': 8, 'defense': 3, 'min_dmg': 10, 'max_dmg': 18, 'price': 36244},
        'Morning Star':    {'klass': 'Thrust', 'level': 9, 'at': 52, 'et': 15, 'rng': 1, 'weight': 2904, 'attack': 9, 'defense': 3, 'min_dmg': 12, 'max_dmg': 20, 'price': 41415},
        'Machete':         {'klass': 'Sword', 'level': 10, 'at': 51, 'et': 15, 'rng': 1, 'weight': 3242, 'attack': 10, 'defense': 3, 'min_dmg': 13, 'max_dmg': 22, 'price': 46586},
        'Katana':          {'klass': 'Sword', 'level': 11, 'at': 50, 'et': 15, 'rng': 1, 'weight': 3580, 'attack': 10, 'defense': 4, 'min_dmg': 14, 'max_dmg': 24, 'price': 51756},
        'Chainsword':      {'klass': 'Sword', 'level': 12, 'at': 49, 'et': 15, 'rng': 1, 'weight': 3918, 'attack': 11, 'defense': 4, 'min_dmg': 16, 'max_dmg': 26, 'price': 56927},
        'Combat Knife':    {'klass': 'Sword', 'level': 13, 'at': 48, 'et': 15, 'rng': 1, 'weight': 4256, 'attack': 12, 'defense': 4, 'min_dmg': 17, 'max_dmg': 28, 'price': 62097},
        'Gladius':         {'klass': 'Sword', 'level': 14, 'at': 47, 'et': 15, 'rng': 1, 'weight': 4594, 'attack': 12, 'defense': 4, 'min_dmg': 18, 'max_dmg': 30, 'price': 67268},
        'War Axe':         {'klass': 'Thrust', 'level': 15, 'at': 46, 'et': 15, 'rng': 1, 'weight': 4932, 'attack': 13, 'defense': 5, 'min_dmg': 20, 'max_dmg': 32, 'price': 72439},
        'Battle Hammer':   {'klass': 'Thrust', 'level': 16, 'at': 45, 'et': 15, 'rng': 1, 'weight': 5270, 'attack': 13, 'defense': 5, 'min_dmg': 21, 'max_dmg': 34, 'price': 77609},
        'Halberd':         {'klass': 'Thrust', 'level': 17, 'at': 44, 'et': 15, 'rng': 2, 'weight': 5608, 'attack': 14, 'defense': 5, 'min_dmg': 22, 'max_dmg': 36, 'price': 82780},
        'Spear':           {'klass': 'Melee', 'level': 18, 'at': 43, 'et': 15, 'rng': 2, 'weight': 5946, 'attack': 14, 'defense': 5, 'min_dmg': 24, 'max_dmg': 38, 'price': 87950},
        'Power Blade':     {'klass': 'Sword', 'level': 19, 'at': 42, 'et': 15, 'rng': 2, 'weight': 6284, 'attack': 15, 'defense': 6, 'min_dmg': 25, 'max_dmg': 40, 'price': 93121},
        'Shock Baton':     {'klass': 'Thrust', 'level': 20, 'at': 41, 'et': 15, 'rng': 2, 'weight': 6622, 'attack': 15, 'defense': 6, 'min_dmg': 26, 'max_dmg': 42, 'price': 98292},
        'Chain Flail':     {'klass': 'Thrust', 'level': 21, 'at': 40, 'et': 15, 'rng': 2, 'weight': 6960, 'attack': 16, 'defense': 6, 'min_dmg': 28, 'max_dmg': 44, 'price': 103462},
        'Plasma Dagger':   {'klass': 'Sword', 'level': 22, 'at': 39, 'et': 15, 'rng': 2, 'weight': 7298, 'attack': 17, 'defense': 6, 'min_dmg': 29, 'max_dmg': 46, 'price': 108633},
        'Powered Katana':  {'klass': 'Sword', 'level': 23, 'at': 38, 'et': 15, 'rng': 2, 'weight': 7636, 'attack': 17, 'defense': 7, 'min_dmg': 30, 'max_dmg': 48, 'price': 113804},
        'Vibro Axe':       {'klass': 'Thrust', 'level': 24, 'at': 37, 'et': 15, 'rng': 2, 'weight': 7974, 'attack': 18, 'defense': 7, 'min_dmg': 32, 'max_dmg': 50, 'price': 118974},
        'Pulse Hammer':    {'klass': 'Thrust', 'level': 25, 'at': 36, 'et': 15, 'rng': 2, 'weight': 8312, 'attack': 18, 'defense': 7, 'min_dmg': 33, 'max_dmg': 52, 'price': 124145},
        'Gravity Mace':    {'klass': 'Thrust', 'level': 26, 'at': 35, 'et': 15, 'rng': 2, 'weight': 8650, 'attack': 19, 'defense': 7, 'min_dmg': 34, 'max_dmg': 54, 'price': 129316},
        'Mag Blade':       {'klass': 'Sword', 'level': 27, 'at': 34, 'et': 15, 'rng': 2, 'weight': 8988, 'attack': 20, 'defense': 8, 'min_dmg': 36, 'max_dmg': 56, 'price': 134486},
        'Energy Scythe':   {'klass': 'Thrust', 'level': 28, 'at': 33, 'et': 15, 'rng': 2, 'weight': 9326, 'attack': 21, 'defense': 8, 'min_dmg': 37, 'max_dmg': 58, 'price': 139657},
        'Plasma Sword':    {'klass': 'Sword', 'level': 29, 'at': 32, 'et': 15, 'rng': 2, 'weight': 9664, 'attack': 22, 'defense': 8, 'min_dmg': 38, 'max_dmg': 60, 'price': 144828},
        'Omega Blade':     {'klass': 'Sword', 'level': 30, 'at': 30, 'et': 15, 'rng': 2, 'weight': 10000, 'attack': 25, 'defense': 8, 'min_dmg': 40, 'max_dmg': 60, 'price': 150000},

        # firearms
        'Rusty Pistol': {'klass': 'Firearm', 'level': 1, 'at': 50, 'et': 15, 'rng': 10, 'weight': 800, 'attack': 5, 'defense': 0, 'min_dmg': 8, 'max_dmg': 12, 'price': 100, 'ammo': '9mm', 'mag_size': 8},
        '9mm Pistol': {'klass': 'Firearm', 'level': 2, 'at': 49, 'et': 16, 'rng': 10, 'weight': 1786, 'attack': 6, 'defense': 0, 'min_dmg': 10, 'max_dmg': 14, 'price': 34310, 'ammo': '9mm', 'mag_size': 12},
        'Silenced Pistol': {'klass': 'Firearm', 'level': 3, 'at': 48, 'et': 18, 'rng': 10, 'weight': 2771, 'attack': 7, 'defense': 1, 'min_dmg': 12, 'max_dmg': 16, 'price': 68521, 'ammo': '9mm', 'mag_size': 12},
        'Revolver': {'klass': 'Firearm', 'level': 4, 'at': 47, 'et': 19, 'rng': 10, 'weight': 3757, 'attack': 7, 'defense': 1, 'min_dmg': 15, 'max_dmg': 20, 'price': 102731, 'ammo': '45ACP', 'mag_size': 6},
        'Compact SMG': {'klass': 'Firearm', 'level': 5, 'at': 46, 'et': 21, 'rng': 10, 'weight': 4743, 'attack': 8, 'defense': 1, 'min_dmg': 18, 'max_dmg': 24, 'price': 136041, 'ammo': '9mm', 'mag_size': 20},
        'SMG': {'klass': 'Firearm', 'level': 6, 'at': 45, 'et': 22, 'rng': 10, 'weight': 5729, 'attack': 9, 'defense': 2, 'min_dmg': 20, 'max_dmg': 28, 'price': 169352, 'ammo': '9mm', 'mag_size': 30},
        'Tactical SMG': {'klass': 'Firearm', 'level': 7, 'at': 44, 'et': 24, 'rng': 10, 'weight': 6714, 'attack': 10, 'defense': 2, 'min_dmg': 24, 'max_dmg': 34, 'price': 202662, 'ammo': '9mm', 'mag_size': 40},
        'Shotgun': {'klass': 'Firearm', 'level': 8, 'at': 43, 'et': 26, 'rng': 10, 'weight': 7700, 'attack': 11, 'defense': 2, 'min_dmg': 28, 'max_dmg': 40, 'price': 235973, 'ammo': '12g', 'mag_size': 5},
        'Auto Shotgun': {'klass': 'Firearm', 'level': 9, 'at': 42, 'et': 28, 'rng': 10, 'weight': 8686, 'attack': 12, 'defense': 2, 'min_dmg': 32, 'max_dmg': 50, 'price': 269283, 'ammo': '12g', 'mag_size': 8},
        'Hunting Rifle': {'klass': 'Firearm', 'level': 10, 'at': 41, 'et': 30, 'rng': 30, 'weight': 9671, 'attack': 13, 'defense': 3, 'min_dmg': 36, 'max_dmg': 55, 'price': 302593, 'ammo': '7.62mm', 'mag_size': 5},
        'Assault Rifle': {'klass': 'Firearm', 'level': 11, 'at': 40, 'et': 32, 'rng': 30, 'weight': 10657, 'attack': 14, 'defense': 3, 'min_dmg': 40, 'max_dmg': 60, 'price': 335904, 'ammo': '5.56mm', 'mag_size': 30},
        'Carbine': {'klass': 'Firearm', 'level': 12, 'at': 39, 'et': 34, 'rng': 30, 'weight': 11643, 'attack': 15, 'defense': 4, 'min_dmg': 44, 'max_dmg': 65, 'price': 369214, 'ammo': '5.56mm', 'mag_size': 30},
        'Sniper Rifle': {'klass': 'Firearm', 'level': 13, 'at': 38, 'et': 36, 'rng': 30, 'weight': 12629, 'attack': 16, 'defense': 4, 'min_dmg': 50, 'max_dmg': 80, 'price': 402525, 'ammo': '7.62mm', 'mag_size': 5},
        'Battle Rifle': {'klass': 'Firearm', 'level': 14, 'at': 37, 'et': 38, 'rng': 30, 'weight': 13614, 'attack': 17, 'defense': 4, 'min_dmg': 55, 'max_dmg': 90, 'price': 435835, 'ammo': '7.62mm', 'mag_size': 20},
        'LMG': {'klass': 'Firearm', 'level': 15, 'at': 36, 'et': 40, 'rng': 30, 'weight': 14600, 'attack': 18, 'defense': 5, 'min_dmg': 60, 'max_dmg': 95, 'price': 469145, 'ammo': '7.62mm', 'mag_size': 50},
        'Heavy LMG': {'klass': 'Firearm', 'level': 16, 'at': 35, 'et': 42, 'rng': 30, 'weight': 15586, 'attack': 20, 'defense': 5, 'min_dmg': 70, 'max_dmg': 110, 'price': 502456, 'ammo': '7.62mm', 'mag_size': 75},
        'Minigun': {'klass': 'Firearm', 'level': 17, 'at': 34, 'et': 45, 'rng': 30, 'weight': 16571, 'attack': 21, 'defense': 6, 'min_dmg': 80, 'max_dmg': 120, 'price': 535766, 'ammo': '7.62mm', 'mag_size': 200},
        'Grenade Launcher': {'klass': 'Firearm', 'level': 18, 'at': 33, 'et': 48, 'rng': 30, 'weight': 17557, 'attack': 22, 'defense': 6, 'min_dmg': 100, 'max_dmg': 150, 'price': 569077, 'ammo': '40mm', 'mag_size': 1},
        'Rocket Launcher': {'klass': 'Firearm', 'level': 19, 'at': 32, 'et': 50, 'rng': 30, 'weight': 18543, 'attack': 23, 'defense': 6, 'min_dmg': 120, 'max_dmg': 180, 'price': 602387, 'ammo': 'RPG', 'mag_size': 1},
        'Railgun': {'klass': 'Firearm', 'level': 20, 'at': 31, 'et': 52, 'rng': 30, 'weight': 19529, 'attack': 24, 'defense': 6, 'min_dmg': 140, 'max_dmg': 200, 'price': 635697, 'ammo': 'RailSlug', 'mag_size': 5},
        'Laser Pistol': {'klass': 'Firearm', 'level': 21, 'at': 30, 'et': 30, 'rng': 30, 'weight': 20514, 'attack': 25, 'defense': 7, 'min_dmg': 50, 'max_dmg': 80, 'price': 669008, 'ammo': 'EnergyCell', 'mag_size': 20},
        'Laser Rifle': {'klass': 'Firearm', 'level': 22, 'at': 30, 'et': 35, 'rng': 30, 'weight': 21500, 'attack': 26, 'defense': 7, 'min_dmg': 80, 'max_dmg': 120, 'price': 702318, 'ammo': 'EnergyCell', 'mag_size': 30},
        'Plasma Carbine': {'klass': 'Firearm', 'level': 23, 'at': 30, 'et': 38, 'rng': 30, 'weight': 22486, 'attack': 28, 'defense': 8, 'min_dmg': 100, 'max_dmg': 150, 'price': 735629, 'ammo': 'EnergyCell', 'mag_size': 25},
        'Plasma Rifle': {'klass': 'Firearm', 'level': 24, 'at': 30, 'et': 40, 'rng': 30, 'weight': 23471, 'attack': 29, 'defense': 8, 'min_dmg': 120, 'max_dmg': 180, 'price': 768939, 'ammo': 'EnergyCell', 'mag_size': 30},
        'Plasma Cannon': {'klass': 'Firearm', 'level': 25, 'at': 30, 'et': 42, 'rng': 30, 'weight': 24457, 'attack': 30, 'defense': 8, 'min_dmg': 140, 'max_dmg': 200, 'price': 802249, 'ammo': 'EnergyCell', 'mag_size': 10},
        'Gauss Rifle': {'klass': 'Firearm', 'level': 26, 'at': 30, 'et': 45, 'rng': 30, 'weight': 25443, 'attack': 31, 'defense': 8, 'min_dmg': 160, 'max_dmg': 220, 'price': 835560, 'ammo': 'EnergyCell', 'mag_size': 10},
        'Ion Blaster': {'klass': 'Firearm', 'level': 27, 'at': 30, 'et': 48, 'rng': 30, 'weight': 26429, 'attack': 32, 'defense': 9, 'min_dmg': 180, 'max_dmg': 240, 'price': 868870, 'ammo': 'EnergyCell', 'mag_size': 20},
        'Photon Sniper': {'klass': 'Firearm', 'level': 28, 'at': 30, 'et': 50, 'rng': 30, 'weight': 27414, 'attack': 33, 'defense': 10, 'min_dmg': 200, 'max_dmg': 250, 'price': 902181, 'ammo': 'EnergyCell', 'mag_size': 5},
        'Disruptor Cannon': {'klass': 'Firearm', 'level': 29, 'at': 30, 'et': 55, 'rng': 30, 'weight': 28400, 'attack': 34, 'defense': 10, 'min_dmg': 220, 'max_dmg': 250, 'price': 935491, 'ammo': 'EnergyCell', 'mag_size': 5},
        'Omega Railcannon': {'klass': 'Firearm', 'level': 30, 'at': 30, 'et': 60, 'rng': 30, 'weight': 30000, 'attack': 35, 'defense': 12, 'min_dmg': 250, 'max_dmg': 250, 'price': 1000000, 'ammo': 'RailSlug', 'mag_size': 1},

        # hats
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

        'Medkit':      {'klass': 'Usable', 'level': 2, 'weight': 500},
        'Stimulant':   {'klass': 'Usable', 'level': 3, 'weight': 200},

        'Coke':        {'klass': 'Consumable', 'level': 1, 'weight': 400},
        'EnergyDrink': {'klass': 'Consumable', 'level': 1, 'weight': 300},

        'Ammo7mm':      {'klass': 'Ammo', 'level': 2, 'at': 25, 'et': 15, 'rng': 4, 'weight': 25, 'attack': 7, 'defense': 1, 'min_dmg': 3, 'max_dmg': 8},
        'Ammo8mm':      {'klass': 'Ammo', 'level': 2, 'at': 25, 'et': 15, 'rng': 4, 'weight': 40, 'attack': 7, 'defense': 1, 'min_dmg': 3, 'max_dmg': 8},
        'Ammo9mm':      {'klass': 'Ammo', 'level': 3, 'weight': 55},
        'Ammo12Gauge':  {'klass': 'Ammo', 'level': 5, 'weight': 500},
        'Ammo13':       {'klass': 'Ammo', 'level': 7, 'weight': 110},
        '45ACP':        {'klass': 'Ammo', 'level': 6, 'weight': 180},

        'CyberEye':    {'klass': 'Implant', 'level': 6, 'weight': 100, 'marm': 0, 'farm': 0},
        'NeuralLink':  {'klass': 'Implant', 'level': 8, 'weight': 80, 'marm': 0, 'farm': 0},

        'RhinoDeck':   {'klass': 'Deck', 'level': 1,  'weight': 500, 'mcpu': 6},
        'UserDeck':    {'klass': 'Deck', 'level': 5,  'weight': 600, 'mcpu': 9},
        'ControlDeck': {'klass': 'Deck', 'level': 8,  'weight': 1200, 'mcpu': 50},
        'HackingDeck': {'klass': 'Deck', 'level': 16, 'weight': 700, 'mcpu': 30, 'hac': 4},
        'MetaDeck':    {'klass': 'Deck', 'level': 24, 'weight': 700, 'mcpu': 50, 'hac': 5},

        'Move.exe':     {'klass': 'Move',     'level': 1},
        'Strafe.exe':   {'klass': 'Move',     'level': 2},
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
