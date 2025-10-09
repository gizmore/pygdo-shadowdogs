from gdo.base.Trans import t
from gdo.base.Util import Random
from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.SD_QuestVal import SD_QuestVal
from gdo.shadowdogs.city.y2064.Peine.quests.Awakening import Awakening
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class TalkingNPC(SD_NPC):

    def __init__(self):
        super().__init__()

    @classmethod
    def instance(cls):
        return Shadowdogs.LOCATION_NPCS[cls.fqcn()]

    def sd_quest(self) -> type[SD_Quest]|None:
        return Awakening

    @classmethod
    def sd_npc_default_values(cls):
        return {
            'p_race': 'human',
            'p_gender': 'male',
        }

    def q(self) -> SD_Quest|None:
        return self.sd_quest().instance().player(self.get_player())

    def qv_set(self, key: str, val: str='1'):
        SD_QuestVal.qv_set(self.q(), self.get_player(), key, val)
        return self

    def qv_get(self, key: str) -> str:
        return SD_QuestVal.qv_get(self.q(), self.get_player(), key)


    def get_name(self):
        return self.__class__.__name__


    async def on_say(self, player: SD_Player, text: str):
        key = 'msg_sd_talk_default_' + str(Random.mrand(1, 4))
        await self.send_to_player(self.get_player(), key)

    async def say(self, key: str, args: tuple[str|int,...] = None):
        await self.send_to_player(self.get_player(), 'sd_npc_says', (self.__class__.__name__, t(key, args)))

    async def digesting(self):
        return self
