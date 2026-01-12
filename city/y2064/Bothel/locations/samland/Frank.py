from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Frank(TalkingNPC):

    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('sdqs_frank_dux_hello')
        elif text == 'work':
            await self.say('sdqs_frank_dux_work')
        elif text == 'weed':
            await self.say('sdqs_frank_dux_weed')
        elif text == 'home':
            await self.say('sdqs_frank_dux_home')
            await self.give_word(player, 'ninja')
        elif text == 'ninja':
            await self.say('sdqs_frank_dux_ninja')
        else:
            await self.say('sdqs_frank_dux_lost')
