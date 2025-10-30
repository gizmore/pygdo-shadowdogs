from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.home.quest.Purse import Purse
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Theodor(TalkingNPC):

    def sd_quest(self) -> type[SD_Quest]|None:
        return Purse

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        if text == 'hello':
            if q.qv_get('hello'):
                await self.say('sdqs_purse_hello1')
                q.set('hello', '1')
            else:
                await self.say('sdqs_purse_hello2')
                await self.give_word(player, 'quest')
        elif text == 'quest':
            await self.say('sdqs_purse_quest')
            self.qv_set('hello', '2')
            await self.give_word(player, 'yes')
            await self.give_word(player, 'no')
        elif text == 'yes':
            if self.qv_get('hello') == '2':
                await self.q().accept()
                self.qv_set('hello', '3')
                await self.say('sdqs_purse_yes')
            else:
                await self.say('yes_what')
        elif text == 'no':
            if self.qv_get('hello') == '2':
                await self.say('sdqs_purse_no')
                self.qv_set('hello', '1')
            else:
                await self.say('no_what')
        elif text == 'purse':
            if self.qv_get('hello') == '3':
                self.qv_set('hello', '4')
                await self.say('sdqs_purse_purse')
                await self.give_new_items(player, 'TheosPurse', 'gave', self.render_name())
            elif self.qv_get('hello') == '4':
                await self.say('sdqs_purse_purse4')
            else:
                await self.say('sdqs_purse_purse0')
        else:
            await self.say('sdqs_purse_other')
        await self.give_word(player, 'hello')
