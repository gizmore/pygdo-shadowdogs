from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.police.quest.JackPott import JackPott
from gdo.shadowdogs.locations.Location import Location


class EvidenceRoom(Location):

    GIVING: str = '20xSpeed,2xExtasy,100xWeed'

    async def on_search(self, player: 'SD_Player'):
        q = JackPott.instance()
        if q.is_in_quest():
            q.accomplished()
