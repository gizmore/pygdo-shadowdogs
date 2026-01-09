from gdo.shadowdogs.city.y2064.Peine.locations.alfred.npc.Fish import Fish
from gdo.shadowdogs.city.y2064.Peine.locations.alfred.npc.Alfred import Alfred as Alf
from gdo.shadowdogs.city.y2064.Peine.locations.alfred.npc.Ina import Ina
from gdo.shadowdogs.city.y2064.Peine.locations.alfred.npc.Razor import Razor
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Alfred(Location):

    GIVING: str = 'Bottle'

    NPCS: 'list[type[TalkingNPC]]' = [
        Alf,
        Fish,
        Ina,
        Razor,
    ]
