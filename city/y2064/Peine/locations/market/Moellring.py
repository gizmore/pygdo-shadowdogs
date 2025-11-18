from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.market.Etablisment import Etablisment
from gdo.shadowdogs.city.y2064.Peine.locations.market.Rent import Rent
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Moellring(TalkingNPC):

    def sd_quest(self) -> type[SD_Quest]|None:
        return Etablisment

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        q2 = Rent.instance()

        if q2.is_accepted(player):
            if q2.is_accomplished():
                return await self.on_say3(player, text)
            else:
                return await self.on_say2(player, text)

        if text == 'hello':
            await self.say('sdqs_moellring_hello')
        elif text == 'home':
            if q.qv_get('offered') == '1':
                await self.say('sdqs_moellring_home2', (Shadowdogs.display_nuyen(Etablisment.CAUTION_NUYEN),))
                q.qv_set('offered', '2')
            elif q.qv_get('offered') == '3':
                await self.say('sdqs_moellring_home3')
            else:
                await self.say('sdqs_moellring_home1')
                q.qv_set('offered', '1')
        elif text == 'yes':
            if q.qv_get('offered') == '2':
                if player.get_nuyen() < Etablisment.CAUTION_NUYEN:
                    await self.say('sdqs_moellring_no_money')
                else:
                    player.give_nuyen(-Etablisment.CAUTION_NUYEN)
                    await self.say('sdqs_moellring_give_money')
                    await q.accomplished()
                    await self.say('sdqs_moellring_tell_rent', (Shadowdogs.display_nuyen(Rent.RENT), Rent.DUE))
                    await Rent.instance().accept()
            else:
                await self.say('sdqs_moellring_generic_yes')
        elif text == 'no':
            if q.qv_get('offered') == '2':
                await self.say('sdqs_moellring_home_no')
            else:
                await self.say('sdqs_moellring_generic_no')
        else:
            await self.say('sdqs_moellring_what')
            await self.give_word(self.get_player(), 'hello')
        return None

    async def on_say2(self, player: SD_Player, text: str):
        q2 = Rent.instance()
        if text == 'hello':
            await self.say('sdqs_moellring_what')
        else:
            if player.get_nuyen() < Rent.RENT:
                await self.say('sdqs_moellring_no_money2', (Shadowdogs.display_nuyen(Rent.RENT),))
            else:
                player.give_nuyen(-Rent.RENT)
                await self.say('sdqs_moellring_give_money2', (Shadowdogs.display_nuyen(Rent.RENT),))
                await q2.accomplished()

    async def on_say3(self, player: SD_Player, text: str):
        await self.say('sdqs_moellring_what')

