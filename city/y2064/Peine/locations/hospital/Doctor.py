from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.hospital.Aid import Aid
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Doctor(TalkingNPC):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Aid

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        if text == 'hello':
            await self.say('sdqs_aid_hello')
        elif text == 'weed':
            await self.say(f'sdqs_aid_weed')
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
