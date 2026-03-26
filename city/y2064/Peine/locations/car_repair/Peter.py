from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Peter(TalkingNPC):

    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('sdqs_peterg_hello')
        elif text == 'weed':
            await self.say('sdqs_peterg_weed')
        elif text == 'home':
            await self.say('sdqs_peterg_home')
        elif text == 'quest':
            await self.say('sdqs_peterg_quest')
        elif text == 'yes':
            await self.say('sdqs_peterg_yes')
        elif text == 'no':
            await self.say('sdqs_peterg_no')
