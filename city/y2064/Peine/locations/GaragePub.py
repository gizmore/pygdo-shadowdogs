from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.city.y2064.Peine.npcs.garage.Matthew import Matthew
from gdo.shadowdogs.locations.Location import Location


class GaragePub(Location):

    NPCS: list['type[TalkingNPC]'] = [
        Matthew,
    ]
