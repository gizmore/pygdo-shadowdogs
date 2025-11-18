from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Nauen.locations.paulinaue.LoveTake2 import LoveTake2
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Jessy(TalkingNPC):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return LoveTake2

    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('sdqs_paulinchen_hello')
        if text == 'home':
            await self.say('sdqs_paulinchen_home')
        if text == 'work':
            await self.say('sdqs_paulinchen_work')
        if text == 'sex':
            await self.say('sdqs_paulinchen_sex')
            self.qv_set('sex', '1')
        if text == 'weed':
            await self.say('sdqs_paulinchen_weed')
        if text == 'yes':
            if self.qv_get('sex', ''):
                await self.say('sdqs_paulinchen_yes')
                self.qv_set('sex', '')
                await self.q().accomplished()
            else:
                await self.say('yes_what')
        if text == 'no':
            if self.qv_get('sex', ''):
                await self.say('sdqs_paulinchen_no')
                self.qv_set('sex', '')
            else:
                await self.say('no_what')

