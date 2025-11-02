from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.trains.Bottles import Bottles
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Bum(TalkingNPC):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Bottles

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        if text == 'hello':
            await self.say('sd_peine_bum_hello')
        elif text == 'weed':
            await self.say(f'sd_peine_bum_weed')
            q.qv_set('work_count', '1')
        elif text == 'work':
            n = int(q.qv_get('work_count', '0'))
            if n == 0:
                await self.say('sd_peine_bum_work_0')
            else:
                await self.say(f'sd_peine_bum_work_{n}')
                q.qv_set('work_count', str((n + 1) % 3 + 1))
        elif text == 'yes':
            n = int(q.qv_get('work_count', '0'))
            if n == 3:
                await self.say(f'sd_peine_bum_accept')
                await q.accept()
            else:
                await self.say(f'sd_peine_bum_yes')
                q.qv_set('work_count', '0')
        elif text == 'no':
            n = int(q.qv_get('work_count', '0'))
            if n == 3:
                await self.say(f'sd_peine_bum_deny')
                await q.deny()
            else:
                await self.say(f'sd_peine_bum_no')
