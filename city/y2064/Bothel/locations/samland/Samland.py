from gdo.shadowdogs.city.y2064.Bothel.locations.samland.Edeltraut import Edeltraut
from gdo.shadowdogs.city.y2064.Bothel.locations.samland.Frank import Frank
from gdo.shadowdogs.city.y2064.Bothel.locations.samland.Mike import Mike
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Samland(Location):

    NPCS: 'list[type[TalkingNPC]]' = [
        Edeltraut,
        Frank,
        Mike,
    ]
