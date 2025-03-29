import functools

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Util import Strings
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_ItemName import GDT_ItemName
from gdo.shadowdogs.GDT_Modifiers import GDT_Modifiers
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.item.data.items import items


class GDO_Item(GDO):
    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('item_id'),
            GDT_Player('item_owner').not_null(),
            GDT_ItemName('item_name').not_null(),
            GDT_UInt('item_count').not_null().initial('1'),
            GDT_Modifiers('item_mods'),
            GDT_Created('item_created'),
        ]

    @classmethod
    def create(cls, name: str, count: int, player: 'GDO_Player' = None) -> 'GDO_Item':
        return cls.blank({
            'item_owner': player.get_id() if player else None,
            'item_name': Strings.substr_to(name, '_of_', name),
            'item_count': str(count),
            'item_mods': Strings.substr_from(name, '_of_'),
        }).insert()

    @functools.lru_cache
    def get_item(self) -> Item:
        return items.get_item(self.gdo_val('item_name'), self.gdo_val('item_mods'), self.gdo_value('item_count'))

