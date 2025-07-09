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
    SECONDS_PER_SECOND = 12
    SECONDS_PER_HP_SLEEP = 5
    SECONDS_PER_FOODING = 600
    SECONDS_INITIATIVE = 60

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

    DEF_PER_DEX = 1
    DEF_PER_QUI = 1

    MAX_DISTANCE = 32

    @classmethod
    def display_nuyen(cls, nuyen: int) -> str:
        return str(nuyen) + cls.NUYEN
