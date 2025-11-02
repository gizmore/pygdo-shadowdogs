from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.quests.Etablisment import Etablisment
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Mom(TalkingNPC):

    def sd_quest(self) -> type[SD_Quest] | None:
        return Etablisment

    async def on_say(self, player: SD_Player, text: str):
        if text == 'work':
            await self.say('sdqs_etablisment_work')
            await self.give_word(player, 'home')
        elif text == 'home':
            if self.q().is_accepted(player):
                await self.say('sdqs_etablisment_home2')
            else:
                await self.say('sdqs_etablisment_home1')
                await self.q().accept()
        elif text == 'yes' or text == 'no':
            await self.say('sdqs_etablisment_loveyou')
        elif text == 'weed':
            await self.say('sdqs_mom_no_weed')
        else:
            await self.say('sdqs_etablisment_hello')
            await self.give_word(player, 'work')
