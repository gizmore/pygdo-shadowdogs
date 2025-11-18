from gdo.date.Time import Time
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.locations.Railways import Railways


class TrainStation(Railways):

    def sd_travelt_targets(self, player: SD_Player) -> list[tuple[Location, int, int]]:
        return [
            (self.world().World2064.Peine.TrainStation, 59, Time.ONE_HOUR*3),
        ]
