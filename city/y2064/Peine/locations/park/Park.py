from gdo.shadowdogs.city.y2064.Peine.locations.park.Arnecke import Arnecke
from gdo.shadowdogs.city.y2064.Peine.locations.park.Birdbath import Birdbath
from gdo.shadowdogs.city.y2064.Peine.locations.park.Fond import Fond
from gdo.shadowdogs.city.y2064.Peine.locations.park.Jens import Jens
from gdo.shadowdogs.city.y2064.Peine.locations.park.Pond import Pond
from gdo.shadowdogs.city.y2064.Peine.locations.park.Raphael import Raphael
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Park(Location):

    GIVING: str = '2xBottle'

    NPCS: 'list[type[TalkingNPC]]' = [
        Arnecke,
        Jens,
        Raphael,
    ]

    OBSTACLES_INSIDE: list[Obstacle] = [
        Fond('Fond'),
        Pond('Pond'),
        Birdbath('Birdbath'),
    ]
