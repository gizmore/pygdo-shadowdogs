from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Object import GDT_Object
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.SD_QuestDone import SD_QuestDone
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class GDT_Quest(WithPlayerGDO, GDT_Object):

    def __init__(self, name: str):
        super().__init__(name)
        self.table(SD_Quest.table())

    def query_gdos(self, val: str) -> list[GDO]:
        if val is None:
            return GDT.EMPTY_LIST
        if val.isdigit():
            return [self.get_player().get_quests()[int(val) - 1]]
        back = []
        val = val.lower()
        for quest in self.get_player().get_quests():
            if val in quest.render_name().lower() or val in quest.render_descr().lower():
                back.append(quest)
        return back
