from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class DejaVu(TalkingNPC):

    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('sdqs_dejavu_hello')
        if text == 'home':
            await self.say('sdqs_dejavu_home')
        if text == 'work':
            await self.say('sdqs_dejavu_work')
        if text == 'weed':
            await self.say('sdqs_dejavu_weed')
