from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Bothel.locations.winkelmann.Carpenter import Carpenter
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Fritz(TalkingNPC):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Carpenter

    async def on_say(self, player: SD_Player, text: str):
        pass
    