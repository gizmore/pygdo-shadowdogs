from gdo.core.GDT_Object import GDT_Object


class GDT_Item(GDT_Object):

    def __init__(self, name: str):
        super().__init__(name)
        from gdo.shadowdogs.GDO_Item import GDO_Item
        self.table(GDO_Item.table())
