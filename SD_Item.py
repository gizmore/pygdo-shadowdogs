from typing import TYPE_CHECKING

from gdo.base.Trans import t
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_Index import GDT_Index
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.item.Item import Item

from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_ItemName import GDT_ItemName
from gdo.shadowdogs.GDT_Modifiers import GDT_Modifiers
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.item.data.items import items


class SD_Item(WithShadowFunc, GDO):

    @classmethod
    def gdo_real_class(cls, vals: dict[str,str]) -> type[GDO]:
        return items.get_klass(vals['item_name'])

    def gdo_table_name(cls) -> str:
        return 'sd_item'

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('item_id'),
            GDT_Player('item_owner').humans().npcs().not_null().initial('1').cascade_delete(),
            GDT_Slot('item_slot').not_null().initial('nexus'),
            GDT_ItemName('item_name').not_null(),
            GDT_Modifiers('item_mods'),
            GDT_UInt('item_count').bytes(2).not_null().initial('1'),
            GDT_Bool('item_hot').not_null().initial('0'), # hot items cannot be sold. most you find from enemies is hot, except random loot based on level, which is rare.
            GDT_UInt('item_duration').bytes(2).not_null().initial('10000'), # duration in 10000/10000 per centimille or sth.
            GDT_Created('item_created'),
            GDT_Index('item_owner_index').index_fields('item_owner'),
        ]

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return self.render_name()

    def get_slot(self) -> str:
        raise ShadowdogsException('err_sd_no_slot_defined_for_item', (self.get_item_name(),))

    def get_owner(self) -> 'SD_Player':
        return self.gdo_value('item_owner')

    def get_item_name(self) -> str:
        return self.gdo_val('item_name')

    def get_modifier_name(self) -> str:
        return self.gdo_val('item_mods')

    def get_count(self) -> int:
        return self.gdo_value('item_count')

    def is_hot(self) -> bool:
        return self.gdo_value('item_hot')

    def get_duration(self) -> int:
        return self.gdo_value('item_duration')

    def modifier_column(self) -> GDT_Modifiers|GDT:
        return self.column('item_mods')

    def use(self, amount: int=1):
        slot = self.gdo_val('item_slot')
        self.increment('item_count', -amount)
        if self.get_count() <= 0:
            if slot == GDT_Slot.INVENTORY:
                self.get_owner().inventory.remove(self)
                self.delete()

    def render_name(self) -> str:
        count = self.get_count()
        name = self.render_name_wc()
        return name if count <= 1 else f"{count}{Shadowdogs.ITEM_COUNT_SEPERATOR}{name}"

    def render_name_wc(self) -> str:
        name = t(self.get_item_name())
        if mod := self.gdo_val('item_mods'):
            return t('item_name_modified', (name, t("sd_of_"+mod)))
        return name
