from gdo.date.Time import Time
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.Peine import Peine
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.locations.Railways import Railways


class BusStop(Railways):

    def sd_travelt_targets(self, player: SD_Player) -> list[tuple[Location, int, int]]:
        targets = [
            (Peine.TrainStation, 20, Time.ONE_MINUTE * 30),
        ]
        return targets
