from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.garage.quest.Baptism import Baptism
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Matthew(TalkingNPC):

    def sd_quest(self) -> type[SD_Quest]|None:
        return Baptism

    async def on_say(self, player: SD_Player, text: str):

        if self.q().is_in_quest(player):
            if self.q().check_accomplished():
                await self.say('sdqs_matthew_accomplished')
                await self.q().accomplished()
            else:
                await self.say('sdqs_matthew_more_kills')
        elif text == "work":
            await self.say('sdqs_matthew_work')
        elif text == "home":
            n = self.q().qv_get_inced('home', player, 5)
            await self.say(f'sdqs_matthew_home_{n}')
        elif text == "yes":
            n = int(self.q().qv_get('home'))
            if n == 5:
                await self.say('sdqs_matthew_accept')
                await self.q().accept()
            else:
                await self.say('sdqs_matthew_yes')
            self.q().qv_set('home', '0')
        elif text == "no":
            n = int(self.q().qv_get('home'))
            if n == 5:
                await self.say('sdqs_matthew_deny')
                await self.q().deny()
            else:
                await self.say('sdqs_matthew_no')
                self.q().qv_set('home', '0')
        else:
            await self.say('sdqs_matthew_hello')
