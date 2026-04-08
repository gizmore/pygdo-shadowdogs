from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Felix(TalkingNPC):

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        if text == 'hello':
            await self.say('sdqs_felix_hello')
        elif text == 'weed':
            await self.say('sdqs_felix_weed')
        elif text == 'home':
            await self.say('sdqs_felix_home')
        elif text == 'quest':
            if not self.qv_get('q'):
                await self.say('sdqs_felix_quest')
                self.qv_set('q', '1')
            else:
                await self.say('sdqs_felix_quest2')
        elif text == 'yes':
            if not self.qv_get('q'):
                await self.say('sdqs_felix_yes')
            else:
                await self.say('sdqs_felix_yes2')
                self.qv_set('q', '')
                await q.accept()
        elif text == 'no':
            await self.say('sdqs_felix_no')
            self.qv_set('q', '')

