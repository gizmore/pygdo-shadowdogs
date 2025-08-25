from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.shadowdogs.SD_Spell import SD_Spell
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.table.MethodQueryTable import MethodQueryTable


class spells(WithShadowMethod, MethodQueryTable):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdspells'

    def gdo_table(self) -> GDO:
        return SD_Spell.table()

    def gdo_query(self) -> GDO:
        return self.gdo_table().select().where(f"sp_player={self.get_player().get_id()}").order('sd_created ASC')
    