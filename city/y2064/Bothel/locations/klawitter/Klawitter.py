from gdo.shadowdogs.city.y2064.Bothel.locations.klawitter.Cord import Cord
from gdo.shadowdogs.city.y2064.Bothel.locations.klawitter.Dad import Dad
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Klawitter(Location):

    NPCS: 'list[type[TalkingNPC]]' = [
        Cord,
        Dad,
    ]
