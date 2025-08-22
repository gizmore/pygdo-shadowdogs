from gdo.base.Util import Random
from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.SD_QuestVal import SD_QuestVal
from gdo.shadowdogs.city.y2064.Peine.quests.Awakening import Awakening


class TalkingNPC(SD_NPC):

    def __init__(self):
        super().__init__()



    def sd_quest(self) -> SD_Quest|None:
        return Awakening.instance()

    def get_name(self):
        return self.__class__.__name__

    async def on_say(self, player: SD_Player, text: str):
        key = 'msg_sd_talk_default_' + str(Random.mrand(1, 4))
        await self.send_to_player(self.get_player(), key)

    def qv_set(self, key: str, val: str='1'):
        SD_QuestVal.qv_set(self.sd_quest(), self.get_player(), key, val)
        return self

    def qv_get(self, key: str) -> str:
        return SD_QuestVal.qv_get(self.sd_quest(), self.get_player(), key)
