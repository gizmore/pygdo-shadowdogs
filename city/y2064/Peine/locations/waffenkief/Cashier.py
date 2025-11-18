from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.waffenkief.Hate import Hate
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Cashier(TalkingNPC):

    def sd_quest(self) -> type[SD_Quest]|None:
        return Hate

    async def on_say(self, player: SD_Player, text: str):
        if self.q().is_in_quest():
            if (self.q().check_accomplished()):
                await self.q().accomplished()
            else:
                await self.say('sdqs_kief_not_done_yet')
        elif text == "hello":
            await self.say('sdqs_kief_hello')
        elif text == "work":
            if not self.qv_get('offered'):
                await self.say('sdqs_kief_work', (Hate.NUM_KILLS, Hate.REWARD_NY))
                self.qv_set('offered', '1')
            else:
                await self.say('sdqs_kief_work_so')
        elif text == "yes":
            if not self.qv_get('offered'):
                await self.say('sdqs_kief_yes_and')
            else:
                await self.say('sdqs_kief_yes')
                await self.q().accept()
        elif text == "no":
            await self.say('sdqs_kief_too_bad')
            self.qv_set('offered', '')
        elif text == "home":
            await self.say('sdqs_kief_home')
        else:
            await self.say('sdqs_kief_else')
