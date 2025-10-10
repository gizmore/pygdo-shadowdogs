from gdo.base.GDO import GDO
from gdo.base.Query import Query
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.SD_KnownWord import SD_KnownWord
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.table.MethodQueryTable import MethodQueryTable


class words(WithShadowMethod, MethodQueryTable):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdwords"

    @classmethod
    def gdo_trig(cls) -> str:
        return "sdkw"

    def gdo_table(self) -> GDO:
        return SD_KnownWord.table()

    def gdo_table_query(self) -> Query:
        player = self.get_player()
        return self.gdo_table().select().join_object('kw_word').where(f"kw_player={player.get_id()}").order('kw_created')

