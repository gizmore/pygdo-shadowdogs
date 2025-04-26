from typing import TYPE_CHECKING

from gdo.core.GDT_Index import GDT_Index
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Util import Strings
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
            GDT_Player('item_owner').not_null(),
            GDT_Slot('item_slot').not_null().initial('inventory'),
            GDT_ItemName('item_name').not_null(),
            GDT_Modifiers('item_mods'),
            GDT_UInt('item_count').bytes(2).not_null().initial('1'),
            GDT_Created('item_created'),
            GDT_Index('item_owner_index').index_fields('item_owner'),
        ]

    @classmethod
    def create(cls, name: str, count: int, player: 'SD_Player' = None) -> 'SD_Item':
        return cls.blank({
            'item_owner': player.get_id() if player else None,
            'item_name': Strings.substr_to(name, Shadowdogs.MODIFIER_SEPERATOR, name),
            'item_count': str(count),
            'item_mods': Strings.substr_from(name, Shadowdogs.MODIFIER_SEPERATOR),
        }).insert()

    def to_value(self, val: str):
        return items.get_item(self.gdo_val('item_name'), self.gdo_value('item_count'), self.gdo_val('item_mods'))

    def get_item_name(self) -> str:
        return self.gdo_val('item_name')

    def get_count(self) -> int:
        return self.gdo_value('item_count')

    def modifier_column(self) -> GDT_Modifiers:
        return self.column('item_mods')

    def render_name(self) -> str:
        col = self.modifier_column()
        if modifiers := col.get_val():
            return f"{self.get_item_name()}{Shadowdogs.MODIFIER_SEPERATOR}{modifiers}"
        return self.get_item_name()
