from gdo.shadowdogs.locations.Location import Location

from gdo.shadowdogs.city.y2088.Peine.npcs.Horus import Horus as Hoe

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_NPC import SD_NPC


class Horus(Location):
    NPCS: list['SD_NPC'] = [
        Hoe,
    ]
