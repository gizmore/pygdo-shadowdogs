from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.Hireling import Hireling


class Lazer(Hireling):
    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('lazer_thm_hello')
        if text == 'home':
            await self.say('lazer_thm_hello')
        if text == 'work':
            await self.say('lazer_thm_hello')
        if text == 'hello':
            await self.say('lazer_thm_hello')
        if text == 'yes':
            await self.say('lazer_thm_hello')
        if text == 'no':
            await self.say('lazer_thm_hello')
