from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.alfred.quest.GirlFriend import GirlFriend
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Ina(TalkingNPC):

    def sd_quest(self) -> type[SD_Quest]|None:
        return GirlFriend

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        if text == 'hello':
            await self.say('sdqs_ina_hello')
            await self.give_word(player, 'goods')
