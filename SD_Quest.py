from importlib import import_module

from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.base.Util import Arrays
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.SD_QuestDone import SD_QuestDone
from gdo.shadowdogs.SD_QuestVal import SD_QuestVal
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

from typing import TYPE_CHECKING

from gdo.shadowdogs.item.Item import Item

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


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
            'q_klass': cls.__module__ + "." + cls.__name__,
        }).insert()

    @classmethod
    def gdo_real_class(cls, vals: dict[str,str]) -> type[GDO]:
        path = vals.get('q_klass') or f"{cls.__module__}.{cls.__name__}"
        mod_path, sep, class_name = path.rpartition('.')
        if not sep:
            raise ValueError(f"q_klass must be 'package.module.Class', got: {path!r}")
        try:
            mod = import_module(mod_path)
        except Exception as e:
            raise ImportError(f"Cannot import module {mod_path!r} (q_klass={path!r}): {e}") from e
        try:
            typ = getattr(mod, class_name)
        except AttributeError as e:
            raise ImportError(f"Module {mod_path!r} has no attribute {class_name!r} (q_klass={path!r})") from e
        if not isinstance(typ, type) or not issubclass(typ, GDO):
            raise TypeError(f"{path!r} is not a subclass of GDO")
        return typ

    @classmethod
    def gdo_base_class(cls) -> type[GDO]:
        return SD_Quest

    def gdo_persistent(self) -> bool:
        return True

    def gdo_columns(self) -> list[GDT]:
        # from gdo.shadowdogs.SD_QuestDone import SD_QuestDone
        # t = SD_QuestDone.table()
        # query_accept = t.select('COUNT(*)').where('qd_accepted IS NOT NULL AND qd_quest=q_id')
        # query_denied = t.select('COUNT(*)').where('qd_declined IS NOT NULL AND qd_quest=q_id')
        # query_solved = t.select('COUNT(*)').where('qd_success IS NOT NULL AND qd_quest=q_id')
        # query_failed = t.select('COUNT(*)').where('qd_failed IS NOT NULL AND qd_quest=q_id')
        return [
            GDT_AutoInc('q_id'),
            GDT_Name('q_name').not_null(),
            GDT_City('q_city').all().not_null(),
            GDT_String('q_klass').not_null().ascii().case_s(),
            GDT_Created('q_created'),
            # GDT_Virtual(GDT_UInt('q_num_accept')).query(query_accept),
            # GDT_Virtual(GDT_UInt('q_num_denied')).query(query_denied),
            # GDT_Virtual(GDT_UInt('q_num_solved')).query(query_solved),
            # GDT_Virtual(GDT_UInt('q_num_failed')).query(query_failed),
        ]

    def reward(self) -> str|None:
        return None

    def reward_xp(self) -> int:
        return 0

    def reward_skills(self, player: 'SD_Player') -> dict[str, int]:
        return GDT.EMPTY_DICT

    def reward_source(self) -> str:
        return self.render_name()

    async def accept(self):
        self.qd().accept(self, self.get_player())
        await self.on_accept()
        await self.send_to_player(self.get_player(), 'msg_sd_quest_accepted', (self.render_title(), self.render_descr()))

    async def on_accept(self):
        pass

    async def deny(self):
        self.qd().deny(self, self.get_player())
        await self.send_to_player(self.get_player(), 'msg_sd_quest_denied', (self.render_title(),))

    async def accomplished(self):
        self.qd().succeed(self, self.get_player())
        await self.on_reward()
        await self.send_to_player(self.get_player(), 'msg_sd_quest_done', (self.render_title(),))

    async def on_reward(self):
        player = self.get_player()
        if items := self.reward():
            await self.give_new_items(player, items, 'reward', self.reward_source())
        if xp := self.reward_xp():
            await self.give_xp(player, xp)
        if skills := self.reward_skills(player):
            out = []
            for field, inc in skills.items():
                player.incb(field, inc)
                out.append(f"{t(field)}({inc})")
            player.save()
            await self.send_to_player(self.get_player(), 'msg_sd_quest_reward_skill', (Arrays.human_join(out),))

    def is_accepted(self, player: 'SD_Player') -> bool:
        return SD_QuestDone.for_player(self, player or self.get_player()).is_accepted()

    def is_accomplished(self) -> bool:
        return SD_QuestDone.for_player(self, self.get_player()).is_accomplished()

    def is_in_quest(self) -> bool:
        return SD_QuestDone.for_player(self, self.get_player()).is_in_quest()


    ######
    # QV #
    ######

    def qv_get(self, key: str, default: str=None, player: 'SD_Player'=None) -> str:
        return SD_QuestVal.qv_get(self, player or Shadowdogs.CURRENT_PLAYER, key, default)

    def qv_set(self, key: str, val: str, player: 'SD_Player'=None):
        SD_QuestVal.qv_set(self, player or Shadowdogs.CURRENT_PLAYER, key, val)
        return self

    ########
    # Give #
    ########
    async def on_give(self, item: Item) -> bool:
        return False

    ##########
    # Render #
    ##########

    def render_name(self):
        return self.render_title()

    def render_title(self) -> str:
        return self.t(f'sdqt_{self.__class__.__name__.lower()}')

    def render_descr(self) -> str:
        return self.t(f'sdqd_{self.__class__.__name__.lower()}')

