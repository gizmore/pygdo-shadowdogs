from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Nauen.locations.forest.Huntastic import Huntastic
from gdo.shadowdogs.npcs.Hireling import Hireling


class Paul(Hireling):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Huntastic

    async def on_say(self, player: SD_Player, text: str):
        if text == "hello":
            await self.say('sdqs_joerg_hello')
            await self.give_word(player, 'sex')
        elif text == "work":
            await self.say('sdqs_joerg_work')
        elif text == "home":
            await self.say('sdqs_joerg_home')
        elif text == "sex":
            await self.say('sdqs_joerg_sex')
            self.qv_set('sex', '1')
        elif text == "yes":
            if self.qv_get('sex', ''):
                await self.say('sdqs_joerg_quest_yes')
                await self.q().accept()
            else:
                await self.say('yes_what')
        elif text == "no":
            if self.qv_get('sex', ''):
                await self.say('sdqs_joerg_quest_no')
                await self.q().deny()
            else:
                await self.say('no_what')
