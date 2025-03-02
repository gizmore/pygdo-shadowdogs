from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_ItemClass import GDT_ItemClass
from gdo.shadowdogs.GDT_Modifiers import GDT_Modifiers
from gdo.shadowdogs.GDT_Player import GDT_Player


class GDO_Item(GDO):
    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('item_id'),
            GDT_Player('item_owner'),
            GDT_ItemClass('item_class'),
            GDT_Modifiers('item_mods'),
            GDT_Created('item_created'),
        ]
