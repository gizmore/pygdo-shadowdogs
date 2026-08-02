from gdo.shadowdogs.city.y2064.Brunswick.locations.school.HeyTaxi import HeyTaxi
from gdo.shadowdogs.engine.World import World
from gdo.shadowdogs.obstacle.Taxi import TaxiBase

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.locations.Location import Location


class Taxi(TaxiBase):

    TAXI_COST = 77

    def sd_get_taxi_target(self, player: 'SD_Player') -> 'Location':
        return World.World2064.Brunswick.ITSchool


