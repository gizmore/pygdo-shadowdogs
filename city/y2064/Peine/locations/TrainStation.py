from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.locations.Railways import Railways


class TrainStation(Railways):

    GIVING: str = "Stone"

    def sd_methods(self) -> list[str]:
        return [
            'sdtravel',
            'sdsearch'
        ]

    def sd_travelt_targets(self, player: SD_Player) -> list[tuple[Location, int, int]]:
        targets = []
        targets.append()
        return  targets
