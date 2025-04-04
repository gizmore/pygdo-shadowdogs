from gdo.shadowdogs.locations.Bedroom import Bedroom
from gdo.shadowdogs.obstacle.Bed import Bed
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Bedroom(Bedroom):
    OBSTACLES: list[Obstacle] = [
        Bed(),
    ]
