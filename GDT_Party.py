from gdo.core.GDT_Object import GDT_Object
from gdo.shadowdogs.GDO_Party import GDO_Party


class GDT_Party(GDT_Object):
    def __init__(self, name: str):
        super().__init__(name)
        self.table(GDO_Party.table())

