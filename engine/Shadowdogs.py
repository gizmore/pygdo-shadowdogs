from typing import TYPE_CHECKING

from gdo.base.Util import Strings

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_NPC import SD_NPC


class Shadowdogs:

    PARTIES: dict[str,'SD_Party'] = {}
    PLAYERS: dict[str,'SD_Player'] = {}
    NPCS: dict[str,'SD_NPC'] = {}

    MODIFIER_SEPERATOR = '_with_'

    NUYEN = 'NY'
    NUYEN_PER_CREDIT = 100

    XP_PER_KARMA = 10

    SECONDS_PER_SECOND = 6
    SECONDS_PER_HP_SLEEP = 5

    MAX_WEIGHT_PER_STRENGTH = 1000

    HP_PER_BODY = 2
    HP_PER_STRENGTH = 1
    HP_PER_LEVEL = 1

    MP_PER_LEVEL = 0.25
    MP_PER_MAGIC = 2
    MP_PER_INTELLIGENCE = 2
    MP_PER_WISDOM = 1
