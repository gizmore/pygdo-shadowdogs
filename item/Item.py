from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.item.data.items import items


class Item:

    _name: str
    _owner: 'SD_Player'
    _count: int
    _modifiers: dict[str,int]

    def __init__(self, name: str):
        self._name = name
        self._owner = None
        self._count = 1
        self._modifiers = {}

    def get_slot(self) -> str:
        raise ShadowdogsException('err_sd_no_slot_defined_for_item')

    def owner(self, player: 'SD_Player'):
        self._owner = player
        return self

    def count(self, count: int):
        self._count = count
        return self

    def modifiers(self, modifiers: dict[str,int]):
        self._modifiers = modifiers
        return self

    def get_default_modifiers(self) -> dict[str, int]:
        return items.ITEMS[self._name]

    def apply(self, player: 'SD_Player'):
        player.modify(self.get_default_modifiers())
        player.modify(self._modifiers)

    def get_attack_time(self) -> float:
        return 30

    def get_equip_time(self) -> int:
        return 0

    def get_unequip_time(self) -> int:
        return self.get_equip_time() // 2
