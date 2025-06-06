from typing import TYPE_CHECKING

from gdo.core.GDT_Index import GDT_Index
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.Item import Item

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_ItemName import GDT_ItemName
from gdo.shadowdogs.GDT_Modifiers import GDT_Modifiers
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.item.data.items import items


class SD_Item(GDO):
    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('item_id'),
            GDT_Player('item_owner').npcs().not_null().initial('1'),
            GDT_Slot('item_slot').not_null().initial('nexus'),
            GDT_ItemName('item_name').not_null(),
            GDT_Modifiers('item_mods'),
            GDT_UInt('item_count').bytes(2).not_null().initial('1'),
            GDT_Created('item_created'),
            GDT_Index('item_owner_index').index_fields('item_owner'),
        ]

    def get_owner(self) -> 'SD_Player':
        return self.gdo_value('item_owner')

    def to_value(self, val: str):
        return items.get_item(self.gdo_val('item_name'), self.gdo_value('item_count'), self.gdo_value('item_mods')).player(self.get_owner())

    def itm(self) -> Item:
        return self.to_value('')

    def get_item_name(self) -> str:
        return self.gdo_val('item_name')

    def get_count(self) -> int:
        return self.gdo_value('item_count')

    def modifier_column(self) -> GDT_Modifiers|GDT:
        return self.column('item_mods')

    def render_name(self) -> str:
        if modifiers := self.modifier_column().get_val():
            return f"{self.get_item_name()}{Shadowdogs.MODIFIER_SEPERATOR}{modifiers}"
        return self.get_item_name()
