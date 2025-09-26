from typing import Any

from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_Virtual import GDT_Virtual
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_QuestVal import SD_QuestVal
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class SD_Quest(WithShadowFunc, GDO):

    QuestDone = None

    @classmethod
    def qd(cls):
        if not cls.QuestDone:
            from gdo.shadowdogs.SD_QuestDone import SD_QuestDone
            cls.QuestDone = SD_QuestDone
        return cls.QuestDone

    @classmethod
    def gdo_table_name(cls) -> str:
        return 'sd_quest'

    @classmethod
    def instance(cls):
        if quest := (cls.table().select().where(f"q_name={GDO.quote(cls.__name__)}").
                     fetch_as(cls).first().exec().fetch_object()):
            return quest
        split = cls.__module__.split('.')
        return cls.blank({
            'q_name': cls.__name__,
            'q_city': f"{split[3]}.{split[4]}",
        }).insert()

    def gdo_persistent(self) -> bool:
        return True

    def gdo_columns(self) -> list[GDT]:
        from gdo.shadowdogs.SD_QuestDone import SD_QuestDone
        t = SD_QuestDone.table()
        query_accept = t.select('COUNT(*)').where('qd_accepted IS NOT NULL AND qd_quest=q_id')
        query_denied = t.select('COUNT(*)').where('qd_declined IS NOT NULL AND qd_quest=q_id')
        query_solved = t.select('COUNT(*)').where('qd_success IS NOT NULL AND qd_quest=q_id')
        query_failed = t.select('COUNT(*)').where('qd_failed IS NOT NULL AND qd_quest=q_id')
        return [
            GDT_AutoInc('q_id'),
            GDT_Name('q_name').not_null(),
            GDT_City('q_city').all().not_null(),
            GDT_Created('q_created'),
            GDT_Virtual(GDT_UInt('q_num_accept')).query(query_accept),
            GDT_Virtual(GDT_UInt('q_num_denied')).query(query_denied),
            GDT_Virtual(GDT_UInt('q_num_solved')).query(query_solved),
            GDT_Virtual(GDT_UInt('q_num_failed')).query(query_failed),
        ]

    def reward(self) -> str|None:
        return None

    def reward_source(self) -> str:
        return self.render_name()

    async def accept(self):
        self.qd().accept(self, self.get_player())
        await self.send_to_player(self.get_player(), 'msg_sd_quest_accepted', (self.render_title(), self.render_descr()))

    async def deny(self):
        self.qd().deny(self, self.get_player())
        await self.send_to_player(self.get_player(), 'msg_sd_quest_denied', (self.render_title(),))

    async def accomplished(self):
        self.qd().succeed(self, self.get_player())
        await self.on_reward()
        await self.send_to_player(self.get_player(), 'msg_sd_quest_done', (self.render_title(),))

    async def on_reward(self):
        if items := self.reward():
            await self.give_new_items(self.get_player(), items, 'reward', self.reward_source())


    ######
    # QV #
    ######

    def qv_get(self, key: str, default: str=None, player: 'SD_Player'=None) -> str:
        return SD_QuestVal.qv_get(self, player or Shadowdogs.CURRENT_PLAYER, key, default)

    def qv_set(self, key: str, val: str, player: 'SD_Player'=None):
        SD_QuestVal.qv_set(self, player or Shadowdogs.CURRENT_PLAYER, key, val)
        return self

    ##########
    # Render #
    ##########

    def render_title(self) -> str:
        return t(f'sdqt_{self.__class__.__name__.lower()}')

    def render_descr(self) -> str:
        return t(f'sdqd_{self.__class__.__name__.lower()}')

