from gdo.core.GDT_Object import GDT_Object
from gdo.shadowdogs.items.Item import Item


class GDT_Item(GDT_Object):

    def __init__(self, name: str):
        super().__init__(name)
        self.table(Item.table())
