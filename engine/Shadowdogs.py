from typing import TYPE_CHECKING

from gdo.base.Util import Strings

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_NPC import SD_NPC


class Shadowdogs:

    NPCS: dict[str,'SD_NPC'] = {}
    PARTIES: dict[str,'SD_Party'] = {}
    PLAYERS: dict[str,'SD_Player'] = {}
    USERMAP: dict[str,'SD_Player'] = {}
    CURRENT_PLAYER: 'SD_Player' = None

    ITEM_COUNT_SEPERATOR = 'x'
    MODIFIER_SEPERATOR = '_of_'
    ITEM_SEPERATOR = ','

    RARE_NO = 35
    RARE_LOW = 21
    RARE_MEDIUM = 12
    RARE_HIGH = 5
    RARE_HIGHER = 3
    RARE_ULTRA = 1

    NUYEN = '¥'
    NUYEN_PER_CREDIT = 250

    RUNNING_LEVEL: int = 5

    XP_PER_KARMA = 10

    SECONDS_PER_TICK = 1
    SECONDS_PER_HP_SLEEP = 30
    SECONDS_PER_FOODING = 1733
    SECONDS_INITIATIVE = 60
    SECONDS_INITIATIVE_BONUS_PER_QUICKNESS = 1
    SECONDS_PER_METER = 10
    METERS_PER_FORWARD = 2

    FOOD_PER_TICK = 1
    WATER_PER_TICK = 2

    MAX_WEIGHT_PER_STRENGTH = 1200
    MAX_WEIGHT_PER_BODY = 350

    HP_PER_BODY = 2
    HP_PER_BODY_SLEEP = 1
    HP_PER_STRENGTH = 1
    HP_PER_LEVEL = 0.5

    MP_PER_MAGIC = 2
    MP_PER_MAGIC_SLEEP = 1
    MP_PER_INTELLIGENCE = 2
    MP_PER_WISDOM = 1
    MP_PER_LEVEL = 0.25

    ATK_PER_DEX = 2
    ATK_PER_QUI = 0.5

    DEF_PER_DEX = 0.5
    DEF_PER_QUI = 0.5

    MAX_DISTANCE = 24

    EXPLORE_ETA_PER_SQKM = 45
    EXPLORE_ETA_BONUS_PER_QUICKNESS = 4
    EXPLORE_NONE_CHANCE_PER_SQKM = 15

    LOOT_CHANCE_NOTHING = 400
    LOOT_CHANCE_EQUIPMENT = 8
    LOOT_CHANCE_EQUIPMENT_PER_LUCK = 1
    LOOT_CHANCE_INVENTORY = 10
    LOOT_CHANCE_INVENTORY_PER_LUCK = 1
    LOOT_CHANCE_RANDOM = 4
    LOOT_CHANCE_RANDOM_PER_LUCK = 1
    LOOT_CHANCE_RANDOM_MODIFIER = 2
    LOOT_CHANCE_RANDOM_MODIFIER_PER_LUCK = 0.5
    LOOT_CHANCE_NUYEN = 15
    LOOT_CHANCE_NUYEN_PER_LUCK = 1
    LOOT_NUYEN_PER_LEVEL = 20
    LOOT_NUYEN_PER_LUCK = 1

    @classmethod
    def display_nuyen(cls, nuyen: int) -> str:
        return str(nuyen) + cls.NUYEN
