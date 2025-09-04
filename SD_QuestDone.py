from gdo.base.GDT import GDT
from gdo.base.GDO import GDO
from gdo.core.GDT_Object import GDT_Object
from gdo.date.Time import Time
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Timestamp import GDT_Timestamp
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class SD_QuestDone(WithShadowFunc, GDO):

    @classmethod
    def for_player(cls, quest: SD_Quest, player: SD_Player) -> 'SD_QuestDone':
        if qd := SD_QuestDone.table().get_by_id(quest.get_id(), player.get_id()):
            return qd
        return SD_QuestDone.blank({
            'qd_quest': quest.get_id(),
            'qd_player': player.get_id(),
        })

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Object('qd_quest').table(SD_Quest.table()).primary(),
            GDT_Player('qd_player').primary(),
            GDT_Created('qd_noticed'),
            GDT_Timestamp('qd_accepted'),
            GDT_Timestamp('qd_declined'),
            GDT_Timestamp('qd_success'),
            GDT_Timestamp('qd_failed'),
        ]

    def is_accepted(self):
        return self.gdo_val('qd_accepted')

    def is_done(self) -> bool:
        return bool(self.gdo_val('qd_declined') or self.gdo_val('qd_success') or self.gdo_val('qd_failed'))

    @classmethod
    def accept(cls, quest: SD_Quest, player: SD_Player) -> 'SD_QuestDone':
        return cls.change_state(quest, player, 'qd_accepted')

    @classmethod
    def decline(cls, quest: SD_Quest, player: SD_Player) -> 'SD_QuestDone':
        return cls.change_state(quest, player, 'qd_declined')

    @classmethod
    def succeed(cls, quest: SD_Quest, player: SD_Player) -> 'SD_QuestDone':
        return cls.change_state(quest, player, 'qd_success')

    @classmethod
    def fail(cls, quest: SD_Quest, player: SD_Player) -> 'SD_QuestDone':
        return cls.change_state(quest, player, 'qd_failed')

    @classmethod
    def change_state(cls, quest: SD_Quest, player: SD_Player, key: str) -> 'SD_QuestDone':
        qd = cls.for_player(quest, player)
        if not qd.gdo_val(key):
            qd.save_val(key, Time.get_date())
        return qd
