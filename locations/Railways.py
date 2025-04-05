from gdo.shadowdogs.GDO_Player import GDO_Player
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Railways(Location):

    def get_targets(self, player: GDO_Player) -> list[tuple[City, int, int]]:
        return []
