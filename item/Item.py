import functools
from typing import TYPE_CHECKING, Iterator

from gdo.base.GDO import GDO
from gdo.core.GDO_User import GDO_User
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
    # _owner: 'SD_Player|None'
    _count: int
    _modifiers: dict[str, int]

    def __init__(self, name: str):
        self._name = name
        # self._owner = None
        self._count = 1
        self._modifiers = GDO.EMPTY_DICT

    def __repr__(self):
        return f"{self.render_name()}"

    def get_slot(self) -> str:
        raise ShadowdogsException('err_sd_no_slot_defined_for_item')

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

    # def owner(self, player: 'SD_Player'):
    #     self._owner = player
    #     return self

    def count(self, count: int):
        self._count = count
        return self

    def modifiers(self, modifiers: dict[str,int]):
        self._modifiers = modifiers
        return self

    def get_default_modifiers(self) -> dict[str, int]:
        return items.ITEMS[self._name]

    def all_modifiers(self) -> Iterator[tuple[str, int]]:
        yield from self.get_default_modifiers().items()
        yield from self._modifiers.items()

    # def get_player(self, user: GDO_User=None) -> 'SD_Player':
    #     return self._owner

    def g(self, field: str) -> int:
        return self.get_player().g(field)

    def dm(self, field: str) -> int:
        return self.get_default_modifiers().get(field)

    def apply(self, player: 'SD_Player'):
        for key, val in self.get_default_modifiers().items():
            key = f"p_{key}"
            if key in player.modified.keys():
                player.apply(key, val)
        if self._modifiers:
            player.modify(self._modifiers)

    def apply_inv(self, player: 'SD_Player'):
        if weight := self.get_default_modifiers().get('weight'):
            player.apply('p_weight', weight)

    def sd_attack_time(self) -> int:
        return self.dm('at')

    def sd_commands(self) -> list[str]:
        return GDO.EMPTY_LIST

    def get_equip_time(self) -> int:
        return self.dm('et')

    def get_unequip_time(self) -> int:
        return self.get_equip_time() // 2
