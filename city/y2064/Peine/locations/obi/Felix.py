from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Felix(TalkingNPC):

    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('sdqs_felix_hello')
        elif text == 'home':
            await self.say('sdqs_felix_home')
        elif text == 'quest':
            await self.say('sdqs_felix_quest')
        elif text == 'yes':
            await self.say('sdqs_felix_yes')
        elif text == 'no':
            await self.say('sdqs_felix_no')

