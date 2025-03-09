from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.item.data.items import items


class GDT_ItemName(GDT_Enum):

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {k: k for k in items.ITEMS.keys()}
