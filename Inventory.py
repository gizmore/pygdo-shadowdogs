from gdo.base.GDO import GDO
from gdo.base.GDT import GDT


class Inventory(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Player(),
            GDT_Item(),
        ]
