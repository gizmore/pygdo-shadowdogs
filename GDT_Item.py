from gdo.core.GDT_Object import GDT_Object


class GDT_Item(GDT_Object):

    SD_Item = None

    def __init__(self, name: str):
        super().__init__(name)
        if not self.__class__.SD_Item:
            from gdo.shadowdogs.SD_Item import SD_Item
            self.__class__.SD_Item = SD_Item
        self.table(self.__class__.SD_Item.table())
