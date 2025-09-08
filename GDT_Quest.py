from gdo.core.GDT_Object import GDT_Object
from gdo.shadowdogs.SD_Quest import SD_Quest


class GDT_Quest(GDT_Object):

    def __init__(self, name: str):
        super().__init__(name)
        self.table(SD_Quest.table())

