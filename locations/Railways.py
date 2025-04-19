from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Railways(Location):

    def get_targets(self, player: SD_Player) -> list[tuple[City, int, int]]:
        return []
