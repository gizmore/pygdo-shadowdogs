from gdo.core.GDT_Object import GDT_Object


class GDT_Party(GDT_Object):
    def __init__(self, name: str):
        super().__init__(name)
        from gdo.shadowdogs.SD_Party import SD_Party
        self.table(SD_Party.table())

