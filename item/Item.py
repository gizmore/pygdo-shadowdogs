import functools
from typing import TYPE_CHECKING, Iterator

from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Modifier import Modifier
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.data.mapping import mapping

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.item.data.items import items


class Item(WithShadowFunc):

    _name: str
    _count: int
    _modifiers: dict[str, int|str]
    _hot: bool
    _duration: int

    def __init__(self, name: str):
        self._name = name
        self._count = 1
        self._modifiers = GDO.EMPTY_DICT
        self._hot = False
        self._duration = 10000

    def __repr__(self):
        return f"{self.render_name()}{self._modifiers}"

    def get_slot(self) -> str:
        raise ShadowdogsException('err_sd_no_slot_defined_for_item')

    def sd_inv_type(self) -> str:
        return GDT_Slot.INVENTORY

    @functools.cache
    def render_name(self) -> str:
        name = self._name
        if self._modifiers:
            name += Shadowdogs.MODIFIER_SEPERATOR
            joined = []
            for key, val in self._modifiers.items():
                joined.append(mapping.get_fancy_word(key, val))
            name += ",".join(joined)
        return self._name

    def count(self, count: int):
        self._count = count
        return self

    def modifiers(self, modifiers: dict[str,int]):
        self._modifiers = modifiers
        return self

    def hot(self, hot: bool):
        self._hot = hot
        return self

    def duration(self, duration: int):
        self._duration = duration
        return self

    def get_default_modifiers(self) -> dict[str, int|str]:
        return items.ITEMS[self._name]

    def all_modifiers(self) -> Iterator[tuple[str, int]]:
        yield from self.get_default_modifiers().items()
        yield from self._modifiers.items()

    def g(self, field: str) -> int:
        return self.get_player().g(field)

    def dm(self, field: str) -> str:
        return self.get_default_modifiers().get(field)

    def dmi(self, field: str) -> int:
        return int(self.dm(field))

    def apply(self, player: 'SD_Player'):
        list(self.apply_cb(player))
        return self

    def apply_cb(self, player: 'SD_Player'):
        player_keys = player.modified.keys()
        for key, val in self.get_default_modifiers().items():
            key = f"p_{key}"
            if key in player_keys:
                player.apply(key, val)
                yield key, val
        if self._modifiers:
            for key, val in self._modifiers.items():
                key = f"p_{key}"
                if key in player_keys:
                    player.apply(key, val)
                    yield key, val
                return self

    def apply_inv(self, player: 'SD_Player'):
        if weight := self.dm('weight'):
            player.apply('p_weight', int(weight))

    def sd_attack_time(self) -> int:
        return self.dmi('at')

    def sd_commands(self) -> list[str]:
        return GDO.EMPTY_LIST

    def get_equip_time(self) -> int:
        return self.dmi('et') or 0

    def get_unequip_time(self) -> int:
        return self.get_equip_time() // 2
