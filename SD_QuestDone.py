from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Object import GDT_Object
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Timestamp import GDT_Timestamp
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest


class SD_QuestDone(GDO):

    @classmethod
    def for_player(cls, name: str, player: SD_Player) -> 'SD_QuestDone':
        quest = SD_Quest.instance(name, player.get_party().get_city().get_name())
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

    def get_quest(self) -> SD_Quest:
        return SD_Quest.instance(self.gdo_value('qd_quest').gdo_val('q_name'))

    def is_accepted(self):
        pass
