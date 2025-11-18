from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.Jawoll import Jawoll
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Barkeeper(TalkingNPC):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        from gdo.shadowdogs.city.y2064.Peine.locations.garage.quest.Delivery import Delivery
        return Delivery

    async def on_say(self, player: SD_Player, text: str):
        from gdo.shadowdogs.city.y2064.Peine.locations.garage.quest.Delivery import Delivery
        q = self.q()
        if text == "home":
            await self.say('sdqs_barkeeper_home')
        elif text == 'hello':
            await self.say('sdqs_barkeeper_hello')
        elif text == 'work':
            if q.qv_get('work1'):
                await self.say('sdqs_barkeeper_work2')
                await self.give_word(player, 'yes')
                await self.give_word(player, 'no')
            else:
                await self.say('sdqs_barkeeper_work1')
                q.qv_set('work1', '1')
        elif text == 'jawoll':
            await self.say('sdqs_barkeeper_jawoll')
            await self.give_kp(player, self.world().World2064.Peine.Jawoll, False)
        elif text == 'yes':
            if q.qv_get('work1'):
                await self.say('sdqs_barkeeper_accept')
                q.qv_set('work1', '')
                await self.give_new_items(player, f'{Jawoll.BEER_PRICE*Delivery.BEER_COUNT}xNuyen', 'gave', self.render_name())
                await q.accept()
            else:
                await self.say('sdqs_civil_service_what')
        elif text == 'no':
            if q.qv_get('work1'):
                await self.say('sdqs_barkeeper_deny')
                q.qv_set('work1', '')
                await q.deny()
            else:
                await self.say('sdqs_civil_service_no')
        else:
            await self.say('sdqs_barkeeper_else')
