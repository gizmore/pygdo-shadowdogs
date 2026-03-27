from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.park.quests.Hatred import Hatred
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Arnecke(TalkingNPC):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Hatred

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        if text == 'hello':
            await self.say('sdqs_arnecke_hello')
        elif text == 'weed':
            await self.say('sdqs_arnecke_weed')
        elif text == 'home':
            await self.say('sdqs_arnecke_home')
        elif text == 'quest':
            if not self.qv_get('q'):
                await self.say('sdqs_arnecke_quest')
                self.qv_set('q', '1')
            else:
                await self.say('sdqs_arnecke_quest2')
        elif text == 'yes':
            if not self.qv_get('q'):
                await self.say('sdqs_arnecke_yes')
            else:
                await self.say('sdqs_arnecke_yes2')
                self.qv_set('q', '')
                await q.accept()
        elif text == 'no':
            await self.say('sdqs_arnecke_no')
