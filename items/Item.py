from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_ItemClass import GDT_ItemClass


class Item(GDO):
    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('item_name'),
            GDT_ItemClass('item_class'),
            GDT_Created('item_created'),
        ]
