from gdo.base.Trans import t
from gdo.base.Util import Random
from gdo.shadowdogs.GDT_Race import GDT_Race
from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_QuestVal import SD_QuestVal
from gdo.shadowdogs.city.y2064.Peine.locations.home.quest.Awakening import Awakening
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.Item import Item


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Quest import SD_Quest
    from gdo.shadowdogs.quest.DeliveryQuest import DeliveryQuest
    from gdo.shadowdogs.quest.KillQuest import KillQuest


class TalkingNPC(SD_NPC):

    def __init__(self):
        super().__init__()

    @classmethod
    def instance(cls):
        return Shadowdogs.LOCATION_NPCS[cls.fqcn()]

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Awakening

    @classmethod
    def sd_npc_default_values(cls):
        return {
            'p_race': 'human',
            'p_gender': 'male',
        }

    def q(self) -> 'SD_Quest|KillQuest|DeliveryQuest|None':
        return self.sd_quest().instance().player(self.get_player())

    def qv_set(self, key: str, val: str='1'):
        SD_QuestVal.qv_set(self.q(), self.get_player(), key, val)
        return self

    def qv_get(self, key: str, default: str = None) -> str:
        return SD_QuestVal.qv_get(self.q(), self.get_player(), key, default)

    def get_name(self):
        return self.__class__.__name__

    async def on_say(self, player: SD_Player, text: str):
        key = 'msg_sd_talk_default_' + str(Random.mrand(1, 4))
        await self.send_to_player(self.get_player(), key)

    async def say(self, key: str, args: tuple[str|int,...] = None):
        await self.send_to_player(self.get_player(), 'sd_npc_says', (self.__class__.__name__, t(key, args)))

    async def digesting(self):
        return self

    async def on_give(self, item: Item):
        if not await self.q().on_give(item):
            await self.say('sdq_item_no_need')
        item.delete()

    def sd_can_hire(self) -> bool:
        return False

    async def on_hire(self, player: SD_Player, nuyen: int):
        return await self.send_to_player(self.get_player(), 'err_sd_cannot_hire', (self.render_name(),))

    @classmethod
    def blank(cls, vals: dict = None, mark_blank: bool = True) -> 'TalkingNPC':
        obj = super().blank(vals, mark_blank)
        obj.set_values(GDT_Race.BASE[obj.gdo_val('p_race')])
        return obj.modify_all()
