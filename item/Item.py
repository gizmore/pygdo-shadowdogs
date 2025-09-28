from typing import TYPE_CHECKING, Iterator

from gdo.base.GDO import GDO
from gdo.base.Trans import t
from gdo.base.Util import Arrays
from gdo.shadowdogs.GDT_Slot import GDT_Slot

from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.item.data.items import items


class Item(SD_Item):

    _buy_price: int
    _shop_pos: int

    __slots__ = (
        '_buy_price',
        '_shop_pos',
    )

    def __init__(self):
        super().__init__()
        self.fill_defaults()
        self._buy_price = 0
        self._shop_pos = 0

    def __repr__(self):
        return self.render_name()

    def sd_inv_type(self) -> str:
        return GDT_Slot.INVENTORY

    def get_level(self) -> int:
        return self.dmi('level', 1)

    def get_weight(self) -> int:
        return self.dmi('weight', 1337)

    def get_default_modifiers(self) -> dict[str, int|str]:
        return items.ITEMS[self.get_item_name()]

    def all_modifiers(self) -> Iterator[tuple[str, int]]:
        yield from self.get_default_modifiers().items()
        if mods := self.gdo_value('item_mods'):
            yield from mods

    def all_player_modifiers(self) -> Iterator[tuple[str, int]]:
        player = self.get_player()
        player_keys = player.modified.keys()
        for key, value in self.get_default_modifiers().items():
            key = f"p_{key}"
            if key in player_keys:
                yield key, value
        if mod:= self.gdo_value('item_mods'):
            for key, value in mod.items():
                key = f"p_{key}"
                if key in player_keys:
                    yield key, value

    def g(self, field: str) -> int:
        return self.get_player().g(field)

    def dm(self, field: str, default=None) -> str|bool|int:
        return self.get_default_modifiers().get(field, default)

    def dmi(self, field: str, default=0) -> int:
        return int(self.dm(field, default))

    def apply(self, player: 'SD_Player'):
        list(self.apply_cb(player))
        return self

    def apply_cb(self, player: 'SD_Player'):
        for key, val in self.all_player_modifiers():
            player.apply(key, val)
            yield key, val
        return self

    def apply_inv(self, player: 'SD_Player'):
        if weight := self.dm('weight'):
            player.apply('p_weight', int(weight))

    def sd_attack_time(self) -> int:
        return self.dmi('at')

    def sd_commands(self) -> list[str]:
        cmds = []
        for base in self.__class__.__mro__:
            if "sd_commands" in base.__dict__ and base != 'Item':
                cmds.extend(base.sd_commands(self))
        return sorted(set(cmds))

    def get_equip_time(self) -> int:
        return self.dmi('et') or 0

    def get_unequip_time(self) -> int:
        return self.get_equip_time() // 2

    def get_loot_chance(self, default:int=100) -> int:
        return self.dmi('loot_chance', self.get_default_loot_chance(default))

    def get_default_loot_chance(self, default: int=100) -> int:
        return default

    async def on_use(self, target: 'SD_Player|Obstacle'):
        await self.send_to_player(self.get_player(), 'err_sd_item_not_usable', (self.render_name_wc(),))

    def equip(self):
        slot = self.get_slot()
        self.save_val('item_slot', slot)
        self.get_player().save_val(slot, self.get_id()).modify_all()

    def unequip(self):
        self.save_val('item_slot', GDT_Slot.INVENTORY)
        self.get_player().save_val(self.get_slot(), None).modify_all()

    def can_loot(self) -> bool:
        return self.dm('no_loot', False)

    def can_sell(self) -> bool:
        if not self.dm('sell', True):
            return False
        return self.is_hot()

    def buy_price(self, price: int):
        self._buy_price = price
        return self

    def shop_position(self, pos: int):
        self._shop_pos = pos
        return self

    def get_shop_position(self) -> int:
        return self._shop_pos or 0

    def render_slot(self) -> str:
        return t(self.get_slot())

    def render_buy_price(self) -> str:
        return Shadowdogs.display_nuyen(self._buy_price)

    def render_description(self) -> str:
        return self.t(self._name+'_descr')

    def render_examine(self, price: int=None):
        price = price or self._buy_price or self.dmi('price') or t('unknown')
        mods = []
        nmod = ('price', 'klass', 'ef')
        for k,v in self.all_modifiers():
            if k not in nmod:
                mods.append(f"{t(k)}: {v}")
        return t('sd_examine_string', (self.render_name_wc(), t(self.__class__.__name__), self.render_description(), ", ".join(mods), str(price)))

