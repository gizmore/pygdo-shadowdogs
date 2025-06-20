from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.Searchable import Searchable


class Home(Location):

    OBSTACLES: dict[str,list[Obstacle]] = {
        Searchable('Fridge').giving(['Coke']),
    }
