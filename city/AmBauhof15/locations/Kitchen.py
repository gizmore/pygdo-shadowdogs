from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Fridge import Fridge
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Kitchen(Location):

    OBSTACLES: list[Obstacle] = [
        Fridge(),
    ]


