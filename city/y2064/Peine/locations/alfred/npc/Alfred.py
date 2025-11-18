from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.seniorhome.CivilService import CivilService
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Alfred(TalkingNPC):

    def sd_quest(self) -> type[SD_Quest]|None:
        return CivilService

    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('sdqs_alfred_hello')
