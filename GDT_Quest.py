from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Object import GDT_Object
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.SD_QuestDone import SD_QuestDone
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class GDT_Quest(GDT_Object):

    def __init__(self, name: str):
        super().__init__(name)
        self.table(SD_QuestDone.table())

    def query_gdos(self, val: str) -> list[GDO]:
        if val is None:
            return GDT.EMPTY_LIST
        if val.isdigit():
            if gdo := self._table.select().join_object('qd_quest').fetch_as(SD_Quest.table()).where(f"qd_player={Shadowdogs.CURRENT_PLAYER.get_id()}").limit(1, int(val)-1).first().exec().fetch_object():
                return [gdo]
        return self._table.select().join_object('qd_quest').fetch_as(SD_Quest.table()).where(f"qd_player={Shadowdogs.CURRENT_PLAYER.get_id()} AND LOWER(q_name) LIKE '%{GDO.escape(val.lower())}%'").exec().fetch_all()
