from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Stiggi(TalkingNPC):

    async def on_say(self, player: SD_Player, text: str):
        if text == "weed":
            await self.say('sd_stiggi_weed')
            player.va
        elif text == "work":
            await self.say('sd_stiggi_work')
        elif text == "home":
            await self.say('sd_stiggi_home')
        elif text == 'hello' or True:
            await self.say('sd_stiggi_hello')
