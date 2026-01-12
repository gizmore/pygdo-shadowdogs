from gdo.shadowdogs.city.y2064.Bothel.locations.klaus.KlausS import KlausS
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Klaus(Location):

    NPCS: 'list[type[TalkingNPC]]' = [
        KlausS,
    ]

