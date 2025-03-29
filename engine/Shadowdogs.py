from typing import TYPE_CHECKING

from gdo.shadowdogs.city.Peine.Peine import Peine
from gdo.shadowdogs.city.Peine.locations.AmBauhof15 import AmBauhof15
from gdo.shadowdogs.locations.City import City

if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party
    from gdo.shadowdogs.GDO_Player import GDO_Player
    from gdo.shadowdogs.GDO_NPC import GDO_NPC


class Shadowdogs:

    PARTIES: dict[str,'GDO_Party'] = {}
    PLAYERS: dict[str,'GDO_Player'] = {}
    NPCS: dict[str,'GDO_NPC'] = {}

    Peine: Peine = Peine()
    AmBauhof15: AmBauhof15 = AmBauhof15()
    CITIES: dict[str,City] = {
        'Peine': Peine,
        'AmBauhof15': AmBauhof15,
    }

    SECONDS_PER_SECOND = 6
    SECONDS_PER_HP = 5

    MAX_WEIGHT_PER_STRENGTH = 1000
    HP_PER_BODY = 2
    HP_PER_STRENGTH = 1
    HP_PER_LEVEL = 1
    MP_PER_LEVEL = 1
    MP_PER_MAGIC = 3
    MP_PER_INTELLIGENCE = 2
    MP_PER_WISDOM = 1
