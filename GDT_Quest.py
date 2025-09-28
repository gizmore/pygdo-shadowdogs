from gdo.base.GDO import GDO
from gdo.core.GDT_Object import GDT_Object
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.SD_QuestDone import SD_QuestDone
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class GDT_Quest(GDT_Object):

    def __init__(self, name: str):
        super().__init__(name)
        self.table(SD_QuestDone.table())

    def query_gdos(self, val: str) -> list[GDO]:
        if val.isdigit():
            if gdo := self._table.select().join_object('qd_quest').fetch_as(SD_Quest.table()).where(f"qd_player={Shadowdogs.CURRENT_PLAYER.get_id()}{gdt.get_name()} LIKE '%{GDO.escape(val)}%'").exec().fetch_all()
                return [gdo]
        if gdt := self._table.name_column():
            return self._table.select().where(f"{gdt.get_name()} LIKE '%{GDO.escape(val)}%'").exec().fetch_all()
        return GDO.EMPTY_LIST
