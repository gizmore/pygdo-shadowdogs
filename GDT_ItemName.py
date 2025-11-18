from gdo.base.Trans import t
from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.item.data.items import items


class GDT_ItemName(WithShadowFunc, GDT_Enum):

    def __init__(self, name: str):
        super().__init__(name)

    def gdo_choices(self) -> dict:
        return {k: t(k) for k in items.ITEMS.keys()}
