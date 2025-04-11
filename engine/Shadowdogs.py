from typing import TYPE_CHECKING

from gdo.base.Util import Strings

if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party
    from gdo.shadowdogs.GDO_Player import GDO_Player
    from gdo.shadowdogs.GDO_NPC import GDO_NPC


class Shadowdogs:

    PARTIES: dict[str,'GDO_Party'] = {}
    PLAYERS: dict[str,'GDO_Player'] = {}
    NPCS: dict[str,'GDO_NPC'] = {}

    MODIFIER_SEPERATOR = '_with_'

    XP_PER_KARMA = 10

    SECONDS_PER_SECOND = 6
    SECONDS_PER_HP_SLEEP = 5

    MAX_WEIGHT_PER_STRENGTH = 1000

    HP_PER_BODY = 2
    HP_PER_STRENGTH = 1
    HP_PER_LEVEL = 1

    MP_PER_LEVEL = 1
    MP_PER_MAGIC = 3
    MP_PER_INTELLIGENCE = 2
    MP_PER_WISDOM = 1
