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

    ITEMS = {
        # Melee
        'Fists':              {'klass': 'Fists',   'level':  1, 'at': 60, 'et': 15, 'rng': 1,  'weight':   200,  'attack':  4, 'defense': 1, 'min_dmg':  1, 'max_dmg':  4, 'price':     150},
        'Bronze Knuckles':    {'klass': 'Fists',   'level':  2, 'at': 59, 'et': 15, 'rng': 1,  'weight':   538,  'attack':  5, 'defense': 1, 'min_dmg':  2, 'max_dmg':  6, 'price':     450},
        'Steel Knuckles':     {'klass': 'Fists',   'level':  3, 'at': 58, 'et': 15, 'rng': 1,  'weight':   876,  'attack':  5, 'defense': 1, 'min_dmg':  4, 'max_dmg':  8, 'price':     950},
        'Club':               {'klass': 'Thrust',  'level':  4, 'at': 57, 'et': 15, 'rng': 1,  'weight':  1214,  'attack':  6, 'defense': 2, 'min_dmg':  5, 'max_dmg': 10, 'price':    1650},
        'Short Sword':        {'klass': 'Thrust',  'level':  5, 'at': 56, 'et': 15, 'rng': 1,  'weight':  1552,  'attack':  7, 'defense': 2, 'min_dmg':  6, 'max_dmg': 12, 'price':    2550},
        'Sword':              {'klass': 'Thrust',  'level':  6, 'at': 55, 'et': 15, 'rng': 1,  'weight':  1890,  'attack':  7, 'defense': 2, 'min_dmg':  8, 'max_dmg': 14, 'price':    3650},
        'Long Sword':         {'klass': 'Thrust',  'level':  7, 'at': 54, 'et': 15, 'rng': 1,  'weight':  2228,  'attack':  8, 'defense': 3, 'min_dmg':  9, 'max_dmg': 16, 'price':    4950},
        'Small Axe':          {'klass': 'Thrust',  'level':  8, 'at': 53, 'et': 15, 'rng': 1,  'weight':  2566,  'attack':  8, 'defense': 3, 'min_dmg': 10, 'max_dmg': 18, 'price':    6450},
        'Morning Star':       {'klass': 'Thrust',  'level':  9, 'at': 52, 'et': 15, 'rng': 1,  'weight':  2904,  'attack':  9, 'defense': 3, 'min_dmg': 12, 'max_dmg': 20, 'price':    8150},
        'Machete':            {'klass': 'Sword',   'level': 10, 'at': 51, 'et': 15, 'rng': 1,  'weight':  3242,  'attack': 10, 'defense': 3, 'min_dmg': 13, 'max_dmg': 22, 'price':   10050},
        'Katana':             {'klass': 'Sword',   'level': 11, 'at': 50, 'et': 15, 'rng': 1,  'weight':  3580,  'attack': 10, 'defense': 4, 'min_dmg': 14, 'max_dmg': 24, 'price':   12150},
        'Chainsword':         {'klass': 'Sword',   'level': 12, 'at': 49, 'et': 15, 'rng': 1,  'weight':  3918,  'attack': 11, 'defense': 4, 'min_dmg': 16, 'max_dmg': 26, 'price':   14450},
        'Combat Knife':       {'klass': 'Sword',   'level': 13, 'at': 48, 'et': 15, 'rng': 1,  'weight':  4256,  'attack': 12, 'defense': 4, 'min_dmg': 17, 'max_dmg': 28, 'price':   16950},
        'Gladius':            {'klass': 'Sword',   'level': 14, 'at': 47, 'et': 15, 'rng': 1,  'weight':  4594,  'attack': 12, 'defense': 4, 'min_dmg': 18, 'max_dmg': 30, 'price':   19650},
        'War Axe':            {'klass': 'Thrust',  'level': 15, 'at': 46, 'et': 15, 'rng': 1,  'weight':  4932,  'attack': 13, 'defense': 5, 'min_dmg': 20, 'max_dmg': 32, 'price':   22550},
        'Battle Hammer':      {'klass': 'Thrust',  'level': 16, 'at': 45, 'et': 15, 'rng': 1,  'weight':  5270,  'attack': 13, 'defense': 5, 'min_dmg': 21, 'max_dmg': 34, 'price':   25650},
        'Halberd':            {'klass': 'Thrust',  'level': 17, 'at': 44, 'et': 15, 'rng': 2,  'weight':  5608,  'attack': 14, 'defense': 5, 'min_dmg': 22, 'max_dmg': 36, 'price':   28950},
        'Spear':              {'klass': 'Melee',   'level': 18, 'at': 43, 'et': 15, 'rng': 2,  'weight':  5946,  'attack': 14, 'defense': 5, 'min_dmg': 24, 'max_dmg': 38, 'price':   32450},
        'Power Blade':        {'klass': 'Sword',   'level': 19, 'at': 42, 'et': 15, 'rng': 2,  'weight':  6284,  'attack': 15, 'defense': 6, 'min_dmg': 25, 'max_dmg': 40, 'price':   36150},
        'Shock Baton':        {'klass': 'Thrust',  'level': 20, 'at': 41, 'et': 15, 'rng': 2,  'weight':  6622,  'attack': 15, 'defense': 6, 'min_dmg': 26, 'max_dmg': 42, 'price':   40050},
        'Chain Flail':        {'klass': 'Thrust',  'level': 21, 'at': 40, 'et': 15, 'rng': 2,  'weight':  6960,  'attack': 16, 'defense': 6, 'min_dmg': 28, 'max_dmg': 44, 'price':   44150},
        'Plasma Dagger':      {'klass': 'Sword',   'level': 22, 'at': 39, 'et': 15, 'rng': 2,  'weight':  7298,  'attack': 17, 'defense': 6, 'min_dmg': 29, 'max_dmg': 46, 'price':   48450},
        'Powered Katana':     {'klass': 'Sword',   'level': 23, 'at': 38, 'et': 15, 'rng': 2,  'weight':  7636,  'attack': 17, 'defense': 7, 'min_dmg': 30, 'max_dmg': 48, 'price':   52950},
        'Vibro Axe':          {'klass': 'Thrust',  'level': 24, 'at': 37, 'et': 15, 'rng': 2,  'weight':  7974,  'attack': 18, 'defense': 7, 'min_dmg': 32, 'max_dmg': 50, 'price':   57650},
        'Pulse Hammer':       {'klass': 'Thrust',  'level': 25, 'at': 36, 'et': 15, 'rng': 2,  'weight':  8312,  'attack': 18, 'defense': 7, 'min_dmg': 33, 'max_dmg': 52, 'price':   62550},
        'Gravity Mace':       {'klass': 'Thrust',  'level': 26, 'at': 35, 'et': 15, 'rng': 2,  'weight':  8650,  'attack': 19, 'defense': 7, 'min_dmg': 34, 'max_dmg': 54, 'price':   67650},
        'Mag Blade':          {'klass': 'Sword',   'level': 27, 'at': 34, 'et': 15, 'rng': 2,  'weight':  8988,  'attack': 20, 'defense': 8, 'min_dmg': 36, 'max_dmg': 56, 'price':   72950},
        'Energy Scythe':      {'klass': 'Thrust',  'level': 28, 'at': 33, 'et': 15, 'rng': 2,  'weight':  9326,  'attack': 21, 'defense': 8, 'min_dmg': 37, 'max_dmg': 58, 'price':   78450},
        'Plasma Sword':       {'klass': 'Sword',   'level': 29, 'at': 32, 'et': 15, 'rng': 2,  'weight':  9664,  'attack': 22, 'defense': 8, 'min_dmg': 38, 'max_dmg': 60, 'price':   84150},
        'Omega Blade':        {'klass': 'Sword',   'level': 30, 'at': 30, 'et': 15, 'rng': 2,  'weight': 10000,  'attack': 25, 'defense': 8, 'min_dmg': 40, 'max_dmg': 60, 'price':   90050},

        # firearms
        'Rusty Pistol':       {'klass': 'Firearm', 'level':  1, 'at': 50, 'et': 15, 'rng': 10, 'weight':   800,  'attack':  5, 'defense': 0, 'min_dmg':  8, 'max_dmg': 12, 'price':     500,   'ammo': '7mm',        'mag_size':  8},
        '9mm Pistol':         {'klass': 'Firearm', 'level':  2, 'at': 49, 'et': 16, 'rng': 10, 'weight':  1786,  'attack':  6, 'defense': 0, 'min_dmg': 10, 'max_dmg': 14, 'price':    1400,   'ammo': '9mm',        'mag_size': 12},
        'Silenced Pistol':    {'klass': 'Firearm', 'level':  3, 'at': 48, 'et': 18, 'rng': 10, 'weight':  2771,  'attack':  7, 'defense': 1, 'min_dmg': 12, 'max_dmg': 16, 'price':    2900,   'ammo': '9mm',        'mag_size': 12},
        'Revolver':           {'klass': 'Firearm', 'level':  4, 'at': 47, 'et': 19, 'rng': 10, 'weight':  3757,  'attack':  7, 'defense': 1, 'min_dmg': 15, 'max_dmg': 20, 'price':    5000,   'ammo': '45ACP',      'mag_size':  6},
        'Compact SMG':        {'klass': 'Firearm', 'level':  5, 'at': 46, 'et': 21, 'rng': 10, 'weight':  4743,  'attack':  8, 'defense': 1, 'min_dmg': 18, 'max_dmg': 24, 'price':    7700,   'ammo': '9mm',        'mag_size': 20},
        'SMG':                {'klass': 'Firearm', 'level':  6, 'at': 45, 'et': 22, 'rng': 10, 'weight':  5729,  'attack':  9, 'defense': 2, 'min_dmg': 20, 'max_dmg': 28, 'price':   11000,   'ammo': '9mm',        'mag_size': 30},
        'Tactical SMG':       {'klass': 'Firearm', 'level':  7, 'at': 44, 'et': 24, 'rng': 10, 'weight':  6714,  'attack': 10, 'defense': 2, 'min_dmg': 24, 'max_dmg': 34, 'price':   14900,   'ammo': '9mm',        'mag_size': 40},
        'Shotgun':            {'klass': 'Firearm', 'level':  8, 'at': 43, 'et': 26, 'rng': 10, 'weight':  7700,  'attack': 11, 'defense': 2, 'min_dmg': 28, 'max_dmg': 40, 'price':   19400,   'ammo': '12g',        'mag_size':  5},
        'Auto Shotgun':       {'klass': 'Firearm', 'level':  9, 'at': 42, 'et': 28, 'rng': 10, 'weight':  8686,  'attack': 12, 'defense': 2, 'min_dmg': 32, 'max_dmg': 50, 'price':   24500,   'ammo': '12g',        'mag_size':  8},
        'Hunting Rifle':      {'klass': 'Firearm', 'level': 10, 'at': 41, 'et': 30, 'rng': 30, 'weight':  9671,  'attack': 13, 'defense': 3, 'min_dmg': 36, 'max_dmg': 55, 'price':   30200,   'ammo': '7mm',        'mag_size':  5},
        'Assault Rifle':      {'klass': 'Firearm', 'level': 11, 'at': 40, 'et': 32, 'rng': 30, 'weight': 10657,  'attack': 14, 'defense': 3, 'min_dmg': 40, 'max_dmg': 60, 'price':   36500,   'ammo': '5mm',        'mag_size': 30},
        'Carbine':            {'klass': 'Firearm', 'level': 12, 'at': 39, 'et': 34, 'rng': 30, 'weight': 11643,  'attack': 15, 'defense': 4, 'min_dmg': 44, 'max_dmg': 65, 'price':   43400,   'ammo': '5mm',        'mag_size': 30},
        'Sniper Rifle':       {'klass': 'Firearm', 'level': 13, 'at': 38, 'et': 36, 'rng': 30, 'weight': 12629,  'attack': 16, 'defense': 4, 'min_dmg': 50, 'max_dmg': 80, 'price':   50900,   'ammo': '7mm',        'mag_size':  5},
        'Battle Rifle':       {'klass': 'Firearm', 'level': 14, 'at': 37, 'et': 38, 'rng': 30, 'weight': 13614,  'attack': 17, 'defense': 4, 'min_dmg': 55, 'max_dmg': 90, 'price':   59000,   'ammo': '7mm',        'mag_size': 20},
        'LMG':                {'klass': 'Firearm', 'level': 15, 'at': 36, 'et': 40, 'rng': 30, 'weight': 14600,  'attack': 18, 'defense': 5, 'min_dmg': 60, 'max_dmg': 95, 'price':   67700,   'ammo': '7mm',        'mag_size': 50},
        'Heavy LMG':          {'klass': 'Firearm', 'level': 16, 'at': 35, 'et': 42, 'rng': 30, 'weight': 15586,  'attack': 20, 'defense': 5, 'min_dmg': 70, 'max_dmg':110, 'price':   77000,   'ammo': '7mm',        'mag_size': 75},
        'Minigun':            {'klass': 'Firearm', 'level': 17, 'at': 34, 'et': 45, 'rng': 30, 'weight': 16571,  'attack': 21, 'defense': 6, 'min_dmg': 80, 'max_dmg':120, 'price':   86900,   'ammo': '7mm',        'mag_size':200},
        'Grenade Launcher':   {'klass': 'Firearm', 'level': 18, 'at': 33, 'et': 48, 'rng': 30, 'weight': 17557,  'attack': 22, 'defense': 6, 'min_dmg':100, 'max_dmg':150, 'price':   97400,   'ammo': '40mm',       'mag_size':  1},
        'Rocket Launcher':    {'klass': 'Firearm', 'level': 19, 'at': 32, 'et': 50, 'rng': 30, 'weight': 18543,  'attack': 23, 'defense': 6, 'min_dmg':120, 'max_dmg':180, 'price':  108500,   'ammo': 'RPG',        'mag_size':  1},
        'Railgun':            {'klass': 'Firearm', 'level': 20, 'at': 31, 'et': 52, 'rng': 30, 'weight': 19529,  'attack': 24, 'defense': 6, 'min_dmg':140, 'max_dmg':200, 'price':  120200,   'ammo': 'RailSlug',   'mag_size':  5},
        'Laser Pistol':       {'klass': 'Firearm', 'level': 21, 'at': 30, 'et': 30, 'rng': 30, 'weight': 20514,  'attack': 25, 'defense': 7, 'min_dmg': 50, 'max_dmg': 80, 'price':  265100,   'ammo': 'EnergyCell', 'mag_size': 20},
        'Laser Rifle':        {'klass': 'Firearm', 'level': 22, 'at': 30, 'et': 35, 'rng': 30, 'weight': 21500,  'attack': 26, 'defense': 7, 'min_dmg': 80, 'max_dmg':120, 'price':  290900,   'ammo': 'EnergyCell', 'mag_size': 30},
        'Plasma Carbine':     {'klass': 'Firearm', 'level': 23, 'at': 30, 'et': 38, 'rng': 30, 'weight': 22486,  'attack': 28, 'defense': 8, 'min_dmg':100, 'max_dmg':150, 'price':  317900,   'ammo': 'EnergyCell', 'mag_size': 25},
        'Plasma Rifle':       {'klass': 'Firearm', 'level': 24, 'at': 30, 'et': 40, 'rng': 30, 'weight': 23471,  'attack': 29, 'defense': 8, 'min_dmg':120, 'max_dmg':180, 'price':  346100,   'ammo': 'EnergyCell', 'mag_size': 30},
        'Plasma Cannon':      {'klass': 'Firearm', 'level': 25, 'at': 30, 'et': 42, 'rng': 30, 'weight': 24457,  'attack': 30, 'defense': 8, 'min_dmg':140, 'max_dmg':200, 'price':  375500,   'ammo': 'EnergyCell', 'mag_size': 10},
        'Gauss Rifle':        {'klass': 'Firearm', 'level': 26, 'at': 30, 'et': 45, 'rng': 30, 'weight': 25443,  'attack': 31, 'defense': 8, 'min_dmg':160, 'max_dmg':220, 'price':  406100,   'ammo': 'EnergyCell', 'mag_size': 10},
        'Ion Blaster':        {'klass': 'Firearm', 'level': 27, 'at': 30, 'et': 48, 'rng': 30, 'weight': 26429,  'attack': 32, 'defense': 9, 'min_dmg':180, 'max_dmg':240, 'price':  437900,   'ammo': 'EnergyCell', 'mag_size': 20},
        'Photon Sniper':      {'klass': 'Firearm', 'level': 28, 'at': 30, 'et': 50, 'rng': 30, 'weight': 27414,  'attack': 33, 'defense':10, 'min_dmg':200, 'max_dmg':250, 'price':  470900,   'ammo': 'EnergyCell', 'mag_size':  5},
        'Disruptor Cannon':   {'klass': 'Firearm', 'level': 29, 'at': 30, 'et': 55, 'rng': 30, 'weight': 28400,  'attack': 34, 'defense':10, 'min_dmg':220, 'max_dmg':250, 'price':  505100,   'ammo': 'EnergyCell', 'mag_size':  5},
        'Omega Railcannon':   {'klass': 'Firearm', 'level': 30, 'at': 30, 'et': 60, 'rng': 30, 'weight': 30000,  'attack': 35, 'defense':12, 'min_dmg':250, 'max_dmg':250, 'price':  540500,   'ammo': 'RailSlug',   'mag_size':  1},

        # armor
        'TShirt':                 {'klass': 'Armor',   'level':  0, 'et': 40, 'weight':   250,  'marm':  0, 'farm':  0, 'price':      10},
        'Clothes':                {'klass': 'Armor',   'level':  0, 'et': 50, 'weight':   750,  'marm':  1, 'farm':  0, 'price':      40},
        'Jacket':                 {'klass': 'Armor',   'level':  0, 'et': 60, 'weight':  1250,  'marm':  1, 'farm':  1, 'price':      90},
        'LeatherVest':            {'klass': 'Armor',   'level':  1, 'et': 55, 'weight':  1200,  'marm':  2, 'farm':  0, 'price':     300},
        'PaddedJacket':           {'klass': 'Armor',   'level':  2, 'et': 58, 'weight':  1700,  'marm':  2, 'farm':  1, 'price':     900},
        'KevlarVest':             {'klass': 'Armor',   'level':  3, 'et': 60, 'weight':  2000,  'marm':  3, 'farm':  1, 'price':    1900},
        'KevlarPanelVest':        {'klass': 'Armor',   'level':  4, 'et': 60, 'weight':  2400,  'marm':  3, 'farm':  2, 'price':    3300},
        'TacticalVest':           {'klass': 'Armor',   'level':  5, 'et': 65, 'weight':  2500,  'marm':  4, 'farm':  2, 'price':    5000},
        'RiotArmor':              {'klass': 'Armor',   'level':  6, 'et': 66, 'weight':  8000,  'marm':  6, 'farm':  3, 'price':    7100},
        'BallisticVest':          {'klass': 'Armor',   'level':  7, 'et': 66, 'weight':  4000,  'marm':  4, 'farm':  4, 'price':    9500},
        'NanoFiberSuit':          {'klass': 'Armor',   'level':  8, 'et': 70, 'weight':  1800,  'marm':  5, 'farm':  3, 'price':   12300},
        'PlateCarrierCeramic':    {'klass': 'Armor',   'level':  9, 'et': 68, 'weight':  6500,  'marm':  5, 'farm':  6, 'price':   15500},
        'PlateCarrierSteel':      {'klass': 'Armor',   'level': 10, 'et': 69, 'weight':  9000,  'marm':  6, 'farm':  7, 'price':   19000},
        'UHMWPECarrier':          {'klass': 'Armor',   'level': 11, 'et': 70, 'weight':  5000,  'marm':  5, 'farm':  7, 'price':   22900},
        'SAPIPlateRig':           {'klass': 'Armor',   'level': 12, 'et': 71, 'weight':  7000,  'marm':  6, 'farm':  8, 'price':   27100},
        'FullTacticalRig':        {'klass': 'Armor',   'level': 13, 'et': 72, 'weight':  9500,  'marm':  7, 'farm':  8, 'price':   31700},
        'BallisticCoat':          {'klass': 'Armor',   'level': 14, 'et': 73, 'weight':  4000,  'marm':  6, 'farm':  7, 'price':   36700},
        'GrapheneWeave':          {'klass': 'Armor',   'level': 15, 'et': 74, 'weight':  2000,  'marm':  7, 'farm':  7, 'price':   42000},
        'LiquidArmorVest':        {'klass': 'Armor',   'level': 16, 'et': 74, 'weight':  3000,  'marm':  8, 'farm':  7, 'price':   47700},
        'CompositePlateRig':      {'klass': 'Armor',   'level': 17, 'et': 75, 'weight':  6500,  'marm':  7, 'farm':  9, 'price':   53700},
        'SpallGuardCarrier':      {'klass': 'Armor',   'level': 18, 'et': 75, 'weight':  7800,  'marm':  8, 'farm':  9, 'price':   60100},
        'RiotExoVest':            {'klass': 'Armor',   'level': 19, 'et': 76, 'weight': 11000,  'marm': 10, 'farm':  8, 'price':   66900},
        'SWATArmor':              {'klass': 'Armor',   'level': 20, 'et': 77, 'weight': 10500,  'marm':  8, 'farm': 10, 'price':   74000},
        'CeramicSAPI4':           {'klass': 'Armor',   'level': 21, 'et': 78, 'weight':  8000,  'marm':  8, 'farm': 11, 'price':   81500},
        'TitaniumCompositeRig':   {'klass': 'Armor',   'level': 22, 'et': 79, 'weight':  7500,  'marm':  9, 'farm': 11, 'price':   89300},
        'ReactivePlateVest':      {'klass': 'Armor',   'level': 23, 'et': 79, 'weight':  9000,  'marm':  9, 'farm': 12, 'price':   97500},
        'SmartFiberSuit':         {'klass': 'Armor',   'level': 24, 'et': 80, 'weight':  2500,  'marm':  9, 'farm': 12, 'price':  106100},
        'ExoPlateRig':            {'klass': 'Armor',   'level': 25, 'et': 81, 'weight': 12000,  'marm': 11, 'farm': 13, 'price':  115000},
        'BallisticExosuit':       {'klass': 'Armor',   'level': 26, 'et': 82, 'weight': 15000,  'marm': 12, 'farm': 14, 'price':  124300},
        'NanoCompositeCarapace':  {'klass': 'Armor',   'level': 27, 'et': 83, 'weight':  6000,  'marm': 12, 'farm': 15, 'price':  133900},
        'GrapheneCarapace':       {'klass': 'Armor',   'level': 28, 'et': 84, 'weight':  4800,  'marm': 13, 'farm': 16, 'price':  143900},
        'TitanWeaveSuit':         {'klass': 'Armor',   'level': 29, 'et': 85, 'weight':  5500,  'marm': 14, 'farm': 17, 'price':  154300},
        'OblivionAegis':          {'klass': 'Armor',   'level': 30, 'et': 85, 'weight':  7000,  'marm': 15, 'farm': 18, 'price':  165000},

        # boots
        'Sandals':            {'klass': 'Boots',   'level':  0, 'et': 45, 'weight':  183, 'defense':  0, 'marm': 1, 'farm': 0, 'price':       8},
        'RagShoes':           {'klass': 'Boots',   'level':  1, 'et': 31, 'weight':  167, 'defense':  1, 'marm': 0, 'farm': 1, 'price':      40},
        'WoolSlippers':       {'klass': 'Boots',   'level':  2, 'et': 38, 'weight':  165, 'defense':  1, 'marm': 1, 'farm': 0, 'price':      85},
        'Sneakers':           {'klass': 'Boots',   'level':  3, 'et': 37, 'weight':  215, 'defense':  2, 'marm': 1, 'farm': 1, 'price':     160},
        'SteelToes':          {'klass': 'Boots',   'level':  4, 'et': 39, 'weight':  194, 'defense':  3, 'marm': 2, 'farm': 1, 'price':     250},
        'CombatBoots':        {'klass': 'Boots',   'level':  5, 'et': 55, 'weight':  382, 'defense':  1, 'marm': 0, 'farm': 1, 'price':     380},
        'TacticalWalkers':    {'klass': 'Boots',   'level':  6, 'et': 35, 'weight':  201, 'defense':  4, 'marm': 3, 'farm': 1, 'price':     550},
        'ThermalTreads':      {'klass': 'Boots',   'level':  7, 'et': 46, 'weight':  419, 'defense':  4, 'marm': 1, 'farm': 3, 'price':     750},
        'SilentSteps':        {'klass': 'Boots',   'level':  8, 'et': 50, 'weight':  477, 'defense':  4, 'marm': 4, 'farm': 0, 'price':    1000},
        'UrbanGrips':         {'klass': 'Boots',   'level':  9, 'et': 58, 'weight':  318, 'defense':  3, 'marm': 3, 'farm': 0, 'price':    1300},
        'NomadBoots':         {'klass': 'Boots',   'level': 10, 'et': 36, 'weight':  292, 'defense':  4, 'marm': 4, 'farm': 0, 'price':    1600},
        'AnkleGuards':        {'klass': 'Boots',   'level': 11, 'et': 47, 'weight':  529, 'defense':  4, 'marm': 3, 'farm': 1, 'price':    2000},
        'RunnerBoots':        {'klass': 'Boots',   'level': 12, 'et': 55, 'weight':  373, 'defense':  4, 'marm': 3, 'farm': 1, 'price':    2400},
        'PaddedStompers':     {'klass': 'Boots',   'level': 13, 'et': 52, 'weight':  360, 'defense':  4, 'marm': 1, 'farm': 3, 'price':    2850},
        'GravBoots':          {'klass': 'Boots',   'level': 14, 'et': 61, 'weight':  515, 'defense':  4, 'marm': 4, 'farm': 0, 'price':    3300},
        'ReinforcedHeels':    {'klass': 'Boots',   'level': 15, 'et': 68, 'weight':  526, 'defense':  5, 'marm': 2, 'farm': 3, 'price':    3800},
        'SpiderClimbers':     {'klass': 'Boots',   'level': 16, 'et': 58, 'weight':  796, 'defense':  6, 'marm': 6, 'farm': 0, 'price':    4400},
        'ShockAbsorbers':     {'klass': 'Boots',   'level': 17, 'et': 42, 'weight':  597, 'defense':  5, 'marm': 0, 'farm': 5, 'price':    5100},
        'MagStep':            {'klass': 'Boots',   'level': 18, 'et': 65, 'weight':  784, 'defense':  7, 'marm': 3, 'farm': 4, 'price':    5900},
        'VoidWalkers':        {'klass': 'Boots',   'level': 19, 'et': 73, 'weight':  551, 'defense':  8, 'marm': 0, 'farm': 8, 'price':    6800},
        'StealthSoles':       {'klass': 'Boots',   'level': 20, 'et': 63, 'weight':  624, 'defense':  6, 'marm': 2, 'farm': 4, 'price':    7800},
        'RiotBoots':          {'klass': 'Boots',   'level': 21, 'et': 76, 'weight':  678, 'defense':  7, 'marm': 2, 'farm': 5, 'price':    9000},
        'BlastGuards':        {'klass': 'Boots',   'level': 22, 'et': 74, 'weight':  835, 'defense':  7, 'marm': 3, 'farm': 4, 'price':   10300},
        'HazmatTreads':       {'klass': 'Boots',   'level': 23, 'et': 52, 'weight':  560, 'defense':  7, 'marm': 1, 'farm': 6, 'price':   11700},
        'ServoWalkers':       {'klass': 'Boots',   'level': 24, 'et': 56, 'weight':  858, 'defense': 10, 'marm': 5, 'farm': 5, 'price':   13200},
        'AntiGravFeet':       {'klass': 'Boots',   'level': 25, 'et': 78, 'weight':  814, 'defense':  8, 'marm': 1, 'farm': 7, 'price':   14800},
        'PhaseBoots':         {'klass': 'Boots',   'level': 26, 'et': 64, 'weight':  924, 'defense': 10, 'marm': 4, 'farm': 6, 'price':   16500},
        'NightStalkers':      {'klass': 'Boots',   'level': 27, 'et': 72, 'weight':  779, 'defense': 10, 'marm': 8, 'farm': 2, 'price':   18300},
        'TitanGreaves':       {'klass': 'Boots',   'level': 28, 'et': 75, 'weight': 1187, 'defense': 11, 'marm':  6, 'farm': 5, 'price':   20200},
        'WardenTreads':       {'klass': 'Boots',   'level': 29, 'et': 80, 'weight':  955, 'defense': 10, 'marm':  6, 'farm': 4, 'price':   22200},
        'OblivionStriders':   {'klass': 'Boots',   'level': 30, 'et': 75, 'weight':  882, 'defense': 10, 'marm':  2, 'farm': 8, 'price':   24300},

        # trousers
        'Trousers':               {'klass': 'Trousers','level':  0, 'et': 50, 'weight':   600, 'defense':  1, 'marm': 1, 'farm': 0, 'price':      15},
        'Jeans':                  {'klass': 'Trousers','level':  1, 'et': 55, 'weight':   800, 'defense':  1, 'marm': 1, 'farm': 1, 'price':      60},
        'CargoPants':             {'klass': 'Trousers','level':  2, 'et': 56, 'weight':   900, 'defense':  1, 'marm': 1, 'farm': 1, 'price':     130},
        'ReinforcedPants':        {'klass': 'Trousers','level':  3, 'et': 58, 'weight':  1100, 'defense':  2, 'marm': 2, 'farm': 1, 'price':     280},
        'PaddedPants':            {'klass': 'Trousers','level':  4, 'et': 60, 'weight':  1300, 'defense':  2, 'marm': 2, 'farm': 2, 'price':     520},
        'KevlarLeggings':         {'klass': 'Trousers','level':  5, 'et': 60, 'weight':  1400, 'defense':  2, 'marm': 3, 'farm': 1, 'price':     900},
        'TacticalPants':          {'klass': 'Trousers','level':  6, 'et': 62, 'weight':  1600, 'defense':  3, 'marm': 3, 'farm': 2, 'price':    1300},
        'RiotGreaves':            {'klass': 'Trousers','level':  7, 'et': 63, 'weight':  3000, 'defense':  4, 'marm': 2, 'farm': 4, 'price':    1800},
        'BallisticLeggings':      {'klass': 'Trousers','level':  8, 'et': 65, 'weight':  2600, 'defense':  4, 'marm': 3, 'farm': 4, 'price':    2400},
        'NanoFiberPants':         {'klass': 'Trousers','level':  9, 'et': 67, 'weight':  1800, 'defense':  4, 'marm': 4, 'farm': 3, 'price':    3100},
        'CeramicKneeGuards':      {'klass': 'Trousers','level': 10, 'et': 68, 'weight':  2800, 'defense':  5, 'marm': 4, 'farm': 5, 'price':    3900},
        'UHMWPELeggings':         {'klass': 'Trousers','level': 11, 'et': 69, 'weight':  2400, 'defense':  5, 'marm': 4, 'farm': 6, 'price':    4800},
        'SAPIThighPlates':        {'klass': 'Trousers','level': 12, 'et': 70, 'weight':  3200, 'defense':  6, 'marm': 5, 'farm': 6, 'price':    5800},
        'FullTacticalPants':      {'klass': 'Trousers','level': 13, 'et': 71, 'weight':  3500, 'defense':  6, 'marm': 5, 'farm': 7, 'price':    6900},
        'BallisticOverpants':     {'klass': 'Trousers','level': 14, 'et': 72, 'weight':  2600, 'defense':  6, 'marm': 6, 'farm': 7, 'price':    8100},
        'GrapheneWeavePants':     {'klass': 'Trousers','level': 15, 'et': 73, 'weight':  2000, 'defense':  7, 'marm': 6, 'farm': 7, 'price':    9400},
        'LiquidArmorPants':       {'klass': 'Trousers','level': 16, 'et': 73, 'weight':  2600, 'defense':  7, 'marm': 7, 'farm': 7, 'price':   10800},
        'CompositeGreaves':       {'klass': 'Trousers','level': 17, 'et': 74, 'weight':  4200, 'defense':  8, 'marm': 7, 'farm': 8, 'price':   12300},
        'SpallGuardGreaves':      {'klass': 'Trousers','level': 18, 'et': 75, 'weight':  4800, 'defense':  8, 'marm': 8, 'farm': 8, 'price':   13900},
        'RiotExoGreaves':         {'klass': 'Trousers','level': 19, 'et': 76, 'weight':  5200, 'defense':  9, 'marm': 9, 'farm': 7, 'price':   15600},
        'SWATLegArmor':           {'klass': 'Trousers','level': 20, 'et': 77, 'weight':  5000, 'defense':  9, 'marm': 8, 'farm': 9, 'price':   17400},
        'CeramicSAPI4Legs':       {'klass': 'Trousers','level': 21, 'et': 78, 'weight':  4300, 'defense':  9, 'marm': 8, 'farm':10, 'price':   19300},
        'TitaniumCompositeLegs':  {'klass': 'Trousers','level': 22, 'et': 79, 'weight':  4200, 'defense': 10, 'marm': 9, 'farm':11, 'price':   21300},
        'ReactivePlateLegs':      {'klass': 'Trousers','level': 23, 'et': 79, 'weight':  4600, 'defense': 10, 'marm': 9, 'farm':12, 'price':   23400},
        'SmartFiberPants':        {'klass': 'Trousers','level': 24, 'et': 80, 'weight':  2200, 'defense': 10, 'marm':10, 'farm':12, 'price':   25600},
        'ExoLegRig':              {'klass': 'Trousers','level': 25, 'et': 81, 'weight':  5600, 'defense': 11, 'marm':10, 'farm':13, 'price':   27900},
        'BallisticExoLegs':       {'klass': 'Trousers','level': 26, 'et': 82, 'weight':  6200, 'defense': 12, 'marm':11, 'farm':14, 'price':   30300},
        'NanoCompositeCuisses':   {'klass': 'Trousers','level': 27, 'et': 83, 'weight':  3000, 'defense': 12, 'marm':12, 'farm':15, 'price':   32800},
        'GrapheneCuisses':        {'klass': 'Trousers','level': 28, 'et': 84, 'weight':  2600, 'defense': 13, 'marm':12, 'farm':16, 'price':   35400},
        'TitanWeaveCuisses':      {'klass': 'Trousers','level': 29, 'et': 85, 'weight':  3200, 'defense': 14, 'marm':13, 'farm':17, 'price':   38100},
        'OblivionCuisses':        {'klass': 'Trousers','level': 30, 'et': 85, 'weight':  3800, 'defense': 15, 'marm':14, 'farm':18, 'price':   40900},

        # gloves
        'FingerlessGloves':   {'klass': 'Gloves',  'level':  1, 'et': 37, 'weight':   81, 'defense':  1, 'marm': 0, 'farm': 0, 'price':      35},
        'Gloves':             {'klass': 'Gloves',  'level':  0, 'et': 47, 'weight':  135, 'defense':  1, 'marm': 1, 'farm': 1, 'price':       7},
        'WoolGloves':         {'klass': 'Gloves',  'level':  2, 'et': 38, 'weight':  162, 'defense':  1, 'marm': 1, 'farm': 0, 'price':      75},
        'WorkGloves':         {'klass': 'Gloves',  'level':  3, 'et': 52, 'weight':  125, 'defense':  2, 'marm': 1, 'farm': 1, 'price':     140},
        'GripMitts':          {'klass': 'Gloves',  'level':  4, 'et': 45, 'weight':  241, 'defense':  2, 'marm': 2, 'farm': 0, 'price':     225},
        'PaddedGloves':       {'klass': 'Gloves',  'level':  5, 'et': 36, 'weight':  249, 'defense':  3, 'marm': 2, 'farm': 1, 'price':     340},
        'CombatGloves':       {'klass': 'Gloves',  'level':  6, 'et': 26, 'weight':  152, 'defense':  4, 'marm': 0, 'farm': 4, 'price':     495},
        'TacticalGrips':      {'klass': 'Gloves',  'level':  7, 'et': 33, 'weight':  202, 'defense':  3, 'marm': 1, 'farm': 2, 'price':     680},
        'LeatherWraps':       {'klass': 'Gloves',  'level':  8, 'et': 42, 'weight':  330, 'defense':  2, 'marm': 1, 'farm': 1, 'price':     900},
        'KnucklePads':        {'klass': 'Gloves',  'level':  9, 'et': 32, 'weight':  303, 'defense':  5, 'marm': 4, 'farm': 1, 'price':    1170},
        'ShockGloves':        {'klass': 'Gloves',  'level': 10, 'et': 59, 'weight':  249, 'defense':  5, 'marm': 0, 'farm': 5, 'price':    1440},
        'FrictionSkins':      {'klass': 'Gloves',  'level': 11, 'et': 53, 'weight':  419, 'defense':  5, 'marm': 5, 'farm': 0, 'price':    1800},
        'ThermalMitts':       {'klass': 'Gloves',  'level': 12, 'et': 56, 'weight':  263, 'defense':  6, 'marm': 4, 'farm': 2, 'price':    2160},
        'CarbonKnuckles':     {'klass': 'Gloves',  'level': 13, 'et': 62, 'weight':  352, 'defense':  5, 'marm': 1, 'farm': 4, 'price':    2560},
        'ArmorWeaveGloves':   {'klass': 'Gloves',  'level': 14, 'et': 64, 'weight':  341, 'defense':  6, 'marm': 5, 'farm': 1, 'price':    2970},
        'ServoFingers':       {'klass': 'Gloves',  'level': 15, 'et': 59, 'weight':  500, 'defense':  6, 'marm': 5, 'farm': 1, 'price':    3420},
        'AntiSlashGloves':    {'klass': 'Gloves',  'level': 16, 'et': 50, 'weight':  353, 'defense':  7, 'marm': 0, 'farm': 7, 'price':    3960},
        'SparkGuards':        {'klass': 'Gloves',  'level': 17, 'et': 66, 'weight':  572, 'defense':  5, 'marm': 3, 'farm': 2, 'price':    4590},
        'ClimbClaws':         {'klass': 'Gloves',  'level': 18, 'et': 42, 'weight':  533, 'defense':  6, 'marm': 1, 'farm': 5, 'price':    5310},
        'MagGripGloves':      {'klass': 'Gloves',  'level': 19, 'et': 54, 'weight':  581, 'defense':  6, 'marm': 4, 'farm': 2, 'price':    6120},
        'BioPulseGloves':     {'klass': 'Gloves',  'level': 20, 'et': 49, 'weight':  392, 'defense':  7, 'marm':  1, 'farm': 6, 'price':    7020},
        'CryoGraspers':       {'klass': 'Gloves',  'level': 21, 'et': 47, 'weight':  580, 'defense':  9, 'marm':  9, 'farm': 0, 'price':    8100},
        'HazmatGloves':       {'klass': 'Gloves',  'level': 22, 'et': 49, 'weight':  512, 'defense':  9, 'marm':  1, 'farm': 8, 'price':    9270},
        'StealthGrips':       {'klass': 'Gloves',  'level': 23, 'et': 56, 'weight':  597, 'defense':  9, 'marm':  8, 'farm': 1, 'price':   10530},
        'NeuroTouchGloves':   {'klass': 'Gloves',  'level': 24, 'et': 69, 'weight':  713, 'defense':  9, 'marm':  3, 'farm': 6, 'price':   11880},
        'PhaseGrips':         {'klass': 'Gloves',  'level': 25, 'et': 58, 'weight':  720, 'defense':  8, 'marm':  3, 'farm': 5, 'price':   13320},
        'GauntletMK1':        {'klass': 'Gloves',  'level': 26, 'et': 63, 'weight':  710, 'defense':  9, 'marm':  4, 'farm': 5, 'price':   14850},
        'TitanHands':         {'klass': 'Gloves',  'level': 27, 'et': 73, 'weight':  521, 'defense': 10, 'marm':  3, 'farm': 7, 'price':   16470},
        'GravPalms':          {'klass': 'Gloves',  'level': 28, 'et': 62, 'weight':  820, 'defense':  9, 'marm':  5, 'farm': 4, 'price':   18200},
        'WardenGloves':       {'klass': 'Gloves',  'level': 29, 'et': 53, 'weight':  514, 'defense': 11, 'marm':  1, 'farm':10, 'price':   20000},
        'OblivionClaws':      {'klass': 'Gloves',  'level': 30, 'et': 79, 'weight':  636, 'defense': 10, 'marm':  9, 'farm': 1, 'price':   21900},

        # helmets
        'TinfoilCap':         {'klass': 'Helmet',  'level':  0, 'et': 36, 'weight':  283, 'defense':  2, 'marm': 1, 'farm': 1, 'price':       5},
        'DuctTapeHood':       {'klass': 'Helmet',  'level':  1, 'et': 53, 'weight':  243, 'defense':  2, 'marm': 0, 'farm': 2, 'price':     100},
        'BaseballCap':        {'klass': 'Helmet',  'level':  2, 'et': 47, 'weight':  349, 'defense':  1, 'marm': 0, 'farm': 1, 'price':     220},
        'SkiMask':            {'klass': 'Helmet',  'level':  3, 'et': 43, 'weight':  193, 'defense':  2, 'marm': 1, 'farm': 1, 'price':     360},
        'GuyFawkesMask':      {'klass': 'Helmet',  'level':  4, 'et': 43, 'weight':  353, 'defense':  1, 'marm': 1, 'farm': 0, 'price':     520},
        'LeatherHood':        {'klass': 'Helmet',  'level':  5, 'et': 56, 'weight':  395, 'defense':  2, 'marm': 1, 'farm': 1, 'price':     700},
        'CombatHelmet':       {'klass': 'Helmet',  'level':  6, 'et': 50, 'weight':  537, 'defense':  2, 'marm': 0, 'farm': 2, 'price':     900},
        'GasMask':            {'klass': 'Helmet',  'level':  7, 'et': 37, 'weight':  367, 'defense':  4, 'marm': 1, 'farm': 3, 'price':    1120},
        'RiotHelmet':         {'klass': 'Helmet',  'level':  8, 'et': 63, 'weight':  513, 'defense':  4, 'marm': 2, 'farm': 2, 'price':    1360},
        'VisorHelmet':        {'klass': 'Helmet',  'level':  9, 'et': 51, 'weight':  523, 'defense':  3, 'marm': 1, 'farm': 2, 'price':    1620},
        'DigitalHalo':        {'klass': 'Helmet',  'level': 10, 'et': 68, 'weight':  601, 'defense':  4, 'marm': 3, 'farm': 1, 'price':    1900},
        'QuantumVisor':       {'klass': 'Helmet',  'level': 11, 'et': 66, 'weight':  634, 'defense':  5, 'marm': 3, 'farm': 2, 'price':    2200},
        'Balaclava':          {'klass': 'Helmet',  'level': 12, 'et': 64, 'weight':  428, 'defense':  5, 'marm': 0, 'farm': 5, 'price':    2520},
        'TacticalHood':       {'klass': 'Helmet',  'level': 13, 'et': 70, 'weight':  816, 'defense':  5, 'marm': 0, 'farm': 5, 'price':    2860},
        'KevlarCap':          {'klass': 'Helmet',  'level': 14, 'et': 51, 'weight':  573, 'defense':  6, 'marm': 2, 'farm': 4, 'price':    3220},
        'StealthDome':        {'klass': 'Helmet',  'level': 15, 'et': 58, 'weight':  716, 'defense':  7, 'marm': 1, 'farm': 6, 'price':    3600},
        'CryoHelmet':         {'klass': 'Helmet',  'level': 16, 'et': 76, 'weight':  616, 'defense':  6, 'marm': 4, 'farm': 2, 'price':    4000},
        'DroneMask':          {'klass': 'Helmet',  'level': 17, 'et': 51, 'weight':  554, 'defense':  6, 'marm': 4, 'farm': 2, 'price':    4420},
        'EchoVisor':          {'klass': 'Helmet',  'level': 18, 'et': 50, 'weight':  899, 'defense':  8, 'marm': 4, 'farm': 4, 'price':    4860},
        'FirewallHelmet':     {'klass': 'Helmet',  'level': 19, 'et': 50, 'weight':  790, 'defense':  7, 'marm': 5, 'farm': 2, 'price':    5320},
        'ReflectiveHelm':     {'klass': 'Helmet',  'level': 20, 'et': 80, 'weight': 1077, 'defense':  7, 'marm': 5, 'farm': 2, 'price':    5800},
        'EMPCap':             {'klass': 'Helmet',  'level': 21, 'et': 77, 'weight':  853, 'defense':  8, 'marm': 5, 'farm': 3, 'price':    6300},
        'ServoCrown':         {'klass': 'Helmet',  'level': 22, 'et': 77, 'weight':  849, 'defense':  8, 'marm': 6, 'farm': 2, 'price':    6820},
        'NeuroShield':        {'klass': 'Helmet',  'level': 23, 'et': 76, 'weight': 1093, 'defense':  8, 'marm': 2, 'farm': 6, 'price':    7360},
        'HardenedSkull':      {'klass': 'Helmet',  'level': 24, 'et': 65, 'weight': 1249, 'defense':  9, 'marm': 7, 'farm': 2, 'price':    7920},
        'PolymeshHelm':       {'klass': 'Helmet',  'level': 25, 'et': 57, 'weight':  910, 'defense':  9, 'marm': 6, 'farm': 3, 'price':    8500},
        'BioScannerCap':      {'klass': 'Helmet',  'level': 26, 'et': 85, 'weight':  919, 'defense':  8, 'marm': 2, 'farm': 6, 'price':    9100},
        'Shadowvisor':        {'klass': 'Helmet',  'level': 27, 'et': 80, 'weight': 1131, 'defense':  9, 'marm': 4, 'farm': 5, 'price':    9720},
        'MechHelm':           {'klass': 'Helmet',  'level': 28, 'et': 80, 'weight':  864, 'defense': 10, 'marm': 8, 'farm': 2, 'price':   10360},
        'OblivionCrown':      {'klass': 'Helmet',  'level': 29, 'et': 80, 'weight':  972, 'defense': 11, 'marm': 5, 'farm': 6, 'price':   11020},
        'NovaCrest':          {'klass': 'Helmet',  'level': 30, 'et': 64, 'weight': 1267, 'defense': 12, 'marm':  1, 'farm':11, 'price':   11700},

        'RingOfFire':         {'klass': 'Ring',        'level': 17, 'weight':  17, 'str': 2, 'attack': 4},
        'RingOfWind':         {'klass': 'Ring',        'level': 18, 'weight':  17, 'int': 2, 'cha': 2, 'wis': 1},

        # rings
        'PlasticBand':         {'klass': 'Ring',          'level':  0, 'weight':   6, 'defense': 0, 'marm': 0, 'farm': 0, 'price':     20},   # effect: cosmetic; no gameplay bonus
        'CopperLoop':          {'klass': 'Ring',          'level':  1, 'weight':   8, 'defense': 0, 'marm': 0, 'farm': 0, 'price':     50},   # effect: +1% vendor_buy on components
        'SteelBand':           {'klass': 'Ring',          'level':  2, 'weight':  10, 'defense': 0, 'marm': 0, 'farm': 0, 'price':    120},   # effect: -2% fast_travel_cost
        'Ring':                {'klass': 'Ring',          'level':  3, 'weight':  10, 'defense': 0, 'marm': 1, 'farm': 0, 'price':    300},   # effect: +1% rare_loot_chance
        'SignetRing':          {'klass': 'Ring',          'level':  4, 'weight':  12, 'defense': 0, 'marm': 1, 'farm': 0, 'price':    600},   # effect: +2% mission_payout
        'LuckyBand':           {'klass': 'Ring',          'level':  5, 'weight':   9, 'defense': 0, 'marm': 0, 'farm': 1, 'price':    900},   # effect: +1% crit_chance (clamped with weapon caps)
        'CourierSignet':       {'klass': 'Ring',          'level':  6, 'weight':  11, 'defense': 0, 'marm': 0, 'farm': 1, 'price':   1300},   # effect: +5 inventory_slots (stash only, not carry)
        'MechanicBand':        {'klass': 'Ring',          'level':  7, 'weight':  13, 'defense': 0, 'marm': 1, 'farm': 1, 'price':   1800},   # effect: -5% repair_cost
        'MedtechLoop':         {'klass': 'Ring',          'level':  8, 'weight':   8, 'defense': 0, 'marm': 1, 'farm': 0, 'price':   2400},   # effect: +15% medkit_heal
        'QuietStepRing':       {'klass': 'Ring',          'level':  9, 'weight':   7, 'defense': 0, 'marm': 0, 'farm': 1, 'price':   3100},   # effect: -5% encounter_rate while carrying hot items (no laundering)
        'KnuckleGuard':        {'klass': 'Ring',          'level': 10, 'weight':  15, 'defense': 1, 'marm': 0, 'farm': 1, 'price':   3900},   # effect: -5% recoil/spread on SMGs
        'BruteSeal':           {'klass': 'Ring',          'level': 11, 'weight':  16, 'defense': 1, 'marm': 0, 'farm': 1, 'price':   4800},   # effect: +2% melee_damage
        'RingOfTruth':         {'klass': 'Ring',          'level': 12, 'weight':  12, 'defense': 0, 'marm': 0, 'farm': 0, 'price':   6000, 'max_hp': 2},   # effect: +2 max_hp (flat)
        'QuartermasterSeal':   {'klass': 'Ring',          'level': 13, 'weight':  14, 'defense': 0, 'marm': 1, 'farm': 1, 'price':   7500},   # effect: +10% ammo_from_crates
        'BackdoorSignet':      {'klass': 'Ring',          'level': 14, 'weight':  10, 'defense': 0, 'marm': 0, 'farm': 1, 'price':   9100},   # effect: +8% hack_speed (synergy with Backdoor/Rootkit.exe)
        'NetrunnerLoop':       {'klass': 'Ring',          'level': 15, 'weight':   9, 'defense': 0, 'marm': 0, 'farm': 1, 'price':  10800},   # effect: +1 hac_slot (if deck present)
        'AdrenalineBand':      {'klass': 'Ring',          'level': 16, 'weight':  11, 'defense': 0, 'marm': 1, 'farm': 1, 'price':  12600},   # effect: +5% move_speed for 5s after kill (cd 15s)
        'StabilizerRing':      {'klass': 'Ring',          'level': 17, 'weight':  12, 'defense': 0, 'marm': 1, 'farm': 1, 'price':  14700},   # effect: -10% aim_punch / flinch
        'PulseSyncRing':       {'klass': 'Ring',          'level': 18, 'weight':  13, 'defense': 0, 'marm': 1, 'farm': 1, 'price':  17000},   # effect: +5% reload_speed
        'WardLoop':            {'klass': 'Ring',          'level': 19, 'weight':  14, 'defense': 1, 'marm': 1, 'farm': 1, 'price':  19600},   # effect: +10% status_resist (stun/bleed/gas)
        'WeddingRing':         {'klass': 'WeddingRing',   'level': 20, 'weight':  25, 'defense': 0, 'marm': 0, 'farm': 0, 'price':  22500},   # effect: bonded: +1% xp & nuyen when teamed with partner
        'AegisRing':           {'klass': 'Ring',          'level': 21, 'weight':  16, 'defense': 1, 'marm': 1, 'farm': 1, 'price':  25700},   # effect: +50 temp_shield out of combat (regen; cd 60s)
        'ShadowBond':          {'klass': 'Ring',          'level': 22, 'weight':  10, 'defense': 0, 'marm': 1, 'farm': 2, 'price':  29200},   # effect: -10% heat_from_hot_items (can’t make them sellable)
        'OmniPass':            {'klass': 'Ring',          'level': 23, 'weight':  11, 'defense': 0, 'marm': 0, 'farm': 2, 'price':  33000},   # effect: -15% fast_travel_cost
        'PhaseBand':           {'klass': 'Ring',          'level': 24, 'weight':   9, 'defense': 0, 'marm': 2, 'farm': 1, 'price':  37100},   # effect: 1% chance ignore_incoming_hit (cd 60s)
        'TitanBand':           {'klass': 'Ring',          'level': 25, 'weight':  18, 'defense': 1, 'marm': 1, 'farm': 1, 'price':  41600},   # effect: +10% carry_capacity
        'NeuroLinkRing':       {'klass': 'Ring',          'level': 26, 'weight':   8, 'defense': 0, 'marm': 1, 'farm': 2, 'price':  46500},   # effect: +5% scan_speed & +2% hack_success
        'GravClampRing':       {'klass': 'Ring',          'level': 27, 'weight':  19, 'defense': 1, 'marm': 2, 'farm': 1, 'price':  51800},   # effect: +15% climb_speed; -5% fall_damage
        'EchoRing':            {'klass': 'Ring',          'level': 28, 'weight':  12, 'defense': 0, 'marm': 2, 'farm': 1, 'price':  57600},   # effect: +15m enemy_ping_range (synergy with NMap.exe)
        'WardenSignet':        {'klass': 'Ring',          'level': 29, 'weight':  17, 'defense': 1, 'marm': 2, 'farm': 2, 'price':  63900},   # effect: +5% armor_effectiveness
        'OblivionSeal':        {'klass': 'Ring',          'level': 30, 'weight':  20, 'defense': 1, 'marm': 2, 'farm': 2, 'price':  70700},   # effect: +5% payouts & -5% upkeep; unique_equip=1



        '5mm':                {'klass': 'Ammo',    'level':  2, 'weight':  20},
        '7mm':                {'klass': 'Ammo',    'level':  2, 'weight':  25},
        '9mm':                {'klass': 'Ammo',    'level':  3, 'weight':  45},
        '40mm':               {'klass': 'Ammo',    'level':  3, 'weight': 155},
        '12g':                {'klass': 'Ammo',    'level':  5, 'weight': 500},
        '45ACP':              {'klass': 'Ammo',    'level':  6, 'weight': 180},
        'RPG':                {'klass': 'Ammo',    'level': 20, 'weight': 750},
        'EnergyCell':         {'klass': 'Ammo',    'level': 24, 'weight':1180},
        'RailSlug':           {'klass': 'Ammo',    'level': 30, 'weight': 350},

        'Pen':                {'klass': 'Pen',         'weight':  20},
        'MobilePhone':        {'klass': 'MobilePhone', 'weight': 488},

        'Medkit':             {'klass': 'Usable',      'level':  2, 'weight': 500},
        'Stimulant':          {'klass': 'Usable',      'level':  3, 'weight': 200},

        'Coke':               {'klass': 'Consumable',  'level':  1, 'weight': 333, 'price': 3, 'thirst': 15},
        'EnergyDrink':        {'klass': 'Consumable',  'level':  1, 'weight': 200, 'price': 5, 'thirst': 10},
        'Sandwich':           {'klass': 'Consumable',  'level':  1, 'weight': 436, 'price': 6, 'hunger': 10, 'thirst': -3},
        'Water':              {'klass': 'Consumable',  'level':  1, 'weight': 1500, 'price': 10, 'thirst': 50},

        'CyberEye':           {'klass': 'Implant',     'level':  6, 'weight': 100, 'marm': 0, 'farm': 0},
        'NeuralLink':         {'klass': 'Implant',     'level':  8, 'weight':  80, 'marm': 0, 'farm': 0},

        'RhinoDeck':          {'klass': 'Deck',        'level':  1, 'weight':  500, 'mcpu':  6},
        'UserDeck':           {'klass': 'Deck',        'level':  5, 'weight':  600, 'mcpu':  9},
        'ControlDeck':        {'klass': 'Deck',        'level':  8, 'weight': 1200, 'mcpu': 50},
        'HackingDeck':        {'klass': 'Deck',        'level': 16, 'weight':  700, 'mcpu': 30, 'hac': 4},
        'MetaDeck':           {'klass': 'Deck',        'level': 24, 'weight':  700, 'mcpu': 50, 'hac': 5},

        'Move.exe':           {'klass': 'Move',        'level':  1},
        'Strafe.exe':         {'klass': 'Move',        'level':  2},
        'DMA.exe':            {'klass': 'DMA',         'level':  6},
        'Ping4.exe':          {'klass': 'Ping',        'level':  1},
        'Ping6.exe':          {'klass': 'Ping',        'level':  3},
        'Backdoor.exe':       {'klass': 'Backdoor',    'level':  3},
        'Rootkit.exe':        {'klass': 'Backdoor',    'level':  5},
        'Modkit.exe':         {'klass': 'Backdoor',    'level':  8},
        'hydra.exe':          {'klass': 'Hydra',       'level':  4},
        'JTR.exe':            {'klass': 'Hydra',       'level':  7},
        'NMap.exe':           {'klass': 'NMap',        'level':  7},
        'Trace.exe':          {'klass': 'Trace',       'level':  2},
        'TraceNT.exe':        {'klass': 'Trace',       'level':  4},
        'TraceNG.exe':        {'klass': 'Trace',       'level':  6},

        'EmailArmy':          {'klass': 'Email',       'key': 'sd_email_army'},
        'NoteGizmore':        {'klass': 'Note',        'key': 'sd_note_gizmore'},
    }
    KLASSES = {}

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
