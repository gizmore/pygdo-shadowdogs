from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Bothel.locations.winkelmann.Carpenter import Carpenter
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Fritz(TalkingNPC):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Carpenter

    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('sdqs_Fritz_W_hello')
        elif text == 'work':
            if not self.qv_get('work', ''):
                await self.say('sdqs_Fritz_W_work1')
                self.qv_set('work', '1')
            elif self.q().is_in_quest() or self.q().is_done():
                await self.say('sdqs_Fritz_W_work2')
            else:
                await self.say('sdqs_Fritz_W_work3')
        elif text == 'weed':
            await self.say('sdqs_Fritz_W_weed')
        elif text == 'home':
            await self.say('sdqs_Fritz_W_home')
        elif text == 'ninja':
            await self.say('sdqs_Fritz_W_ninja')
        else:
            await self.say('sdqs_Fritz_W_other')

    