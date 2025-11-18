from gdo.base.Util import Random
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.alfred.quest.Jungle import Jungle
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Fish(TalkingNPC):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Jungle

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        if text == 'hello':
            await self.say('sdqs_jungle_hello')
            await self.give_word(player, 'weed')
        elif text == 'weed':
            n = int(self.qv_get('weed', '0'))
            n += 1
            if n > 5: n = 5
            self.qv_set('weed', str(n))
            await self.say(f'sdqs_jungle_weed{n}')
        elif text == 'yes':
            n = int(self.qv_get('weed', '0'))
            if n < 5 or q.is_in_quest():
                await self.say(f'sdqs_jungle_yes')
            else:
                await self.say(f'sdqs_jungle_accept')
                await q.accept()
        elif text == 'no':
            n = int(self.qv_get('weed', '0'))
            if n < 5 or q.is_in_quest():
                await self.say(f'sdqs_jungle_no')
            else:
                await self.say(f'sdqs_jungle_deny')
                await q.deny()
        elif text == 'home':
            await self.say(f'sdqs_jungle_home_'+str(Random.mrand(1, 2)))
        elif text == 'work':
            await self.say(f'sdqs_jungle_work_'+str(Random.mrand(1, 2)))
        else:
            await self.say(f'sdqs_jungle_else')
