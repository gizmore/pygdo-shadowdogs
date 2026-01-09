from gdo.shadowdogs.city.y2064.Peine.locations.thomann.Krozca import Krozca
from gdo.shadowdogs.city.y2064.Peine.locations.thomann.Lazer import Lazer
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
from gdo.shadowdogs.obstacle.Bed import Bed
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class ThomasMannStr(Location):
    
    NPCS: 'list[type[TalkingNPC]]' = [
        Krozca,
        Lazer,
    ]

    OBSTACLES_INSIDE: list[Obstacle] = [
        Bed,
    ]
