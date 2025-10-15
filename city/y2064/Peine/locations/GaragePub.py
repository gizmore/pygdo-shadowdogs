from gdo.shadowdogs.city.y2064.Peine.npcs.garage.Barkeeper import Barkeeper
from gdo.shadowdogs.city.y2064.Peine.npcs.garage.Matthew import Matthew
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class GaragePub(Location):

    NPCS: list[type[TalkingNPC]] = [
        Matthew,
        Barkeeper,
    ]
