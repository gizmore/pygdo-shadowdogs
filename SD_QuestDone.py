from gdo.base.GDT import GDT
from gdo.base.GDO import GDO
from gdo.core.GDT_Object import GDT_Object
from gdo.date.Time import Time
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Timestamp import GDT_Timestamp
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_Quest import SD_Quest


class SD_QuestDone(WithShadowFunc, GDO):

    @classmethod
    def for_player(cls, quest: 'SD_Quest', player: 'SD_Player') -> 'SD_QuestDone':
        if qd := SD_QuestDone.table().get_by_id(quest.get_id(), player.get_id()):
            return qd
        return SD_QuestDone.blank({
            'qd_quest': quest.get_id(),
            'qd_player': player.get_id(),
        }).insert()

    def gdo_columns(self) -> list[GDT]:
        from gdo.shadowdogs.SD_Quest import SD_Quest
        return [
            GDT_Object('qd_quest').table(SD_Quest.table()).primary().cascade_delete(),
            GDT_Player('qd_player').primary().cascade_delete(),
            GDT_Created('qd_noticed'),
            GDT_Timestamp('qd_accepted'),
            GDT_Timestamp('qd_declined'),
            GDT_Timestamp('qd_success'),
            GDT_Timestamp('qd_failed'),
        ]

    def is_accepted(self) -> bool:
        return self.gdo_val('qd_accepted') is not None

    def is_accomplished(self) -> bool:
        return bool(self.gdo_val('qd_success'))

    def is_done(self) -> bool:
        return bool(self.gdo_val('qd_declined') or self.gdo_val('qd_success') or self.gdo_val('qd_failed'))

    def is_in_quest(self):
        return self.is_accepted() and not self.is_done()

    @classmethod
    def accept(cls, quest: 'SD_Quest', player: 'SD_Player') -> 'SD_QuestDone':
        return cls.change_state(quest, player, 'qd_accepted')

    @classmethod
    def decline(cls, quest: 'SD_Quest', player: 'SD_Player') -> 'SD_QuestDone':
        return cls.change_state(quest, player, 'qd_declined')

    @classmethod
    def succeed(cls, quest: 'SD_Quest', player: 'SD_Player') -> 'SD_QuestDone':
        return cls.change_state(quest, player, 'qd_success')

    @classmethod
    def fail(cls, quest: 'SD_Quest', player: 'SD_Player') -> 'SD_QuestDone':
        return cls.change_state(quest, player, 'qd_failed')

    @classmethod
    def change_state(cls, quest: 'SD_Quest', player: 'SD_Player', key: str) -> 'SD_QuestDone':
        player.reload_quests()
        qd = cls.for_player(quest, player)
        if not qd.gdo_val(key):
            qd.save_val(key, Time.get_date())
        return qd
