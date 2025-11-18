from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Krozca(TalkingNPC):

    async def on_say(self, player: SD_Player, text: str):
        if text == "hello":
            await self.say('')
        if text == "work":
            await self.say('')
