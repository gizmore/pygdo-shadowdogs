from gdo.shadowdogs.city.y2064.Peine.locations.park.Fond import Fond
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Park(Location):

    GIVING: str = '2xBottle'

    OBSTACLES_INSIDE: list[Obstacle] = [
        Fond('Fond'),
    ]
