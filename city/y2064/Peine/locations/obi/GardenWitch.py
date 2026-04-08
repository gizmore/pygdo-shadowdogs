from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class GardenWitch(TalkingNPC):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        from gdo.shadowdogs.city.y2064.Peine.locations.obi.Plants import Plants
        return Plants

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        if text == 'hello':
            await self.say('sdqs_plants_hello')
        elif text == 'weed':
            await self.say('sdqs_plants_weed')
        elif text == 'home':
            await self.say('sdqs_plants_home')
        elif text == 'quest':
            if not self.qv_get('q'):
                await self.say('sdqs_plants_quest')
                self.qv_set('q', '1')
            else:
                await self.say('sdqs_plants_quest2')
        elif text == 'yes':
            if not self.qv_get('q'):
                await self.say('sdqs_plants_yes')
            else:
                await self.say('sdqs_plants_yes2')
                self.qv_set('q', '')
                await q.accept()
        elif text == 'no':
            await self.say('sdqs_plants_no')
            self.qv_set('q', '')
