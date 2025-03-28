from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.item.data.items import items


class Item:

    _count: int
    _modifiers: dict[str,int]

    def __init__(self):
        self._count = 1
        self._modifiers = {}

    def get_slot(self) -> str:
        raise ShadowdogsException('err_sd_no_slot_defined_for_item')

    def count(self, count: int):
        self._count = count
        return self

    def modifiers(self, modifiers: dict[str,int]):
        self._modifiers = modifiers
        return self

    def apply(self, player: 'GDO_Player'):
        player.modify(self._modifiers)
        player.modify(items.ITEMS[self.__class__.__name__])
