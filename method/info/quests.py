from gdo.base.GDT import GDT
from gdo.base.GDO import GDO
from gdo.base.Render import Mode
from gdo.base.Result import Result
from gdo.base.ResultArray import ResultArray
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.table.MethodTable import MethodTable


class quests(WithShadowMethod, MethodTable):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdquests"

    @classmethod
    def gdo_trig(cls) -> str:
        return "sdqus"

    def gdo_ordered(self) -> bool:
        return False

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_City('city').not_null().default_current().positional(),
            # GDT_Enum('type').choices({'open': self.t('sd_qu_open'), 'failed': self.t('sd_qu_failed'), 'denied': self.t('sd_qu_denied'), 'done': self.t('sd_qu_done')}).initial('open'),
        ]

    def get_city(self) -> str:
        return self.param_val('city')

    def gdo_table(self) -> GDO:
        return SD_Quest.table()

    # def get_type(self) -> str:
    #     return self.param_val('type')

    def gdo_render_title(self) -> str:
        return self.t('mt_shadowdogs_quests', (self.get_num_results(), self.param_value('city').render_name()))

    # def gdo_table_query(self) -> Query:
    #     query = SD_QuestDone.table().select().fetch_as(SD_Quest.table()).join_object('qd_quest').where(f"qd_player={self.get_player().get_id()} AND q_city={self.quote(self.get_city())}").order('qd_noticed ASC')
    #     type = self.get_type()
    #     if type == 'open': query.where("qd_declined IS NULL and qd_success IS NULL AND qd_failed IS NULL")
    #     elif type == 'failed': query.where("qd_failed IS NOT NULL")
    #     elif type == 'denied': query.where("qd_declined IS NOT NULL")
    #     elif type == 'done': query.where("qd_success IS NOT NULL")
    #     return query

    def gdo_table_result(self) -> Result:
        return ResultArray(self.get_player().get_quests(), self.gdo_table())


    def render_gdo(self, gdo: GDO, mode: Mode) -> any:
        self._curr_table_row_id += 1
        return self.t('sd_quest', (self._curr_table_row_id, gdo.render_name()))
