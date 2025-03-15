from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Item import GDT_Item
from gdo.shadowdogs.GDT_Player import GDT_Player


class GDO_Inventory(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('inv_id'),
            GDT_Player('inv_player').not_null(),
            GDT_Item('inv_item').not_null(),
            GDT_Created('inv_created'),
        ]
