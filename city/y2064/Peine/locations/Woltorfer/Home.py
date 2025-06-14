from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Home(Location):

    OBSTACLES: dict[str,list[Obstacle]] = {
        Searchable('Fridge', )
    }
