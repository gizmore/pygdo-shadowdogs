from gdo.date.Time import Time
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.quests.Etablisment import Etablisment
from gdo.shadowdogs.city.y2064.Peine.quests.Rent import Rent
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Matthew(TalkingNPC):

    # def sd_quest(self) -> type[SD_Quest]|None:
    #     return Etablisment

    async def on_say(self, player: SD_Player, text: str):
        await self.say('sdqs_matthew_hello')
