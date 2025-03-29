from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Park(Location):

    def sd_obstacles(self) -> list[Obstacle]:
        return []
