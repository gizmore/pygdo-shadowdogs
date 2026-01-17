from gdo.shadowdogs.city.y2064.Oberg.locations.granny.Ruth import Ruth
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Granny(Location):

    GIVING: str = 'Intolerance'

    NPCS: 'list[type[TalkingNPC]]' = [
        Ruth,
    ]
