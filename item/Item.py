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
    from gdo.shadowdogs.SD_Item import SD_Item
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.item.data.items import items


class Item(WithShadowFunc):

    _name: str
    _count: int
    _modifiers: dict[str, int|str]
    _hot: bool
    _duration: int
    _sd_item: 'SD_Item|None'

    def __init__(self, name: str):
        self._name = name
        self._count = 1
        self._modifiers = GDO.EMPTY_DICT
        self._hot = False
        self._duration = 10000
        self._sd_item = None

    def __repr__(self):
        return f"{self.render_name()}{self._modifiers}"

    def get_slot(self) -> str:
        raise ShadowdogsException('err_sd_no_slot_defined_for_item')

    def get_level(self) -> int:
        return self.dmi('level', 1)

    def get_count(self) -> int:
        if self._sd_item:
            return self._sd_item.get_count()
        return self._count

    def get_weight(self) -> int:
        return self.dmi('weight', 0)

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

    def modifiers(self, modifiers: dict[str,int]):
        self._modifiers = modifiers
        return self

    def item(self, item: 'SD_Item'):
        self._sd_item = item
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

    def all_player_modifiers(self) -> Iterator[tuple[str, int]]:
        player = self.get_player()
        player_keys = player.modified.keys()
        for key, value in self.get_default_modifiers().items():
            key = f"p_{key}"
            if key in player_keys:
                yield key, value
        if self._modifiers:
            for key, value in self._modifiers.items():
                key = f"p_{key}"
                if key in player_keys:
                    yield key, value

    def g(self, field: str) -> int:
        return self.get_player().g(field)

    def dm(self, field: str, default=None) -> str:
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
        return GDO.EMPTY_LIST

    def get_equip_time(self) -> int:
        return self.dmi('et') or 0

    def get_unequip_time(self) -> int:
        return self.get_equip_time() // 2

    def get_loot_chance(self, default:int=100) -> int:
        return self.dmi('loot_chance', self.get_default_loot_chance(default))

    def get_default_loot_chance(self, default: int=100) -> int:
        return default

    def get_default_count(self) -> int:
        return 1

    def count(self, param):
        pass

    async def on_use(self, target: 'SD_Player|Obstacle'):
        await self.send_to_player(self.get_player(), 'err_sd_item_not_usable')
