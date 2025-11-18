import re

from gdo.base.Util import Strings
from gdo.core.GDT_String import GDT_String

from typing import TYPE_CHECKING

from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.locations.Store import Store

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class GDT_ItemArg(WithShadowFunc, GDT_String):

    _equipment: bool
    _inventory: bool
    _store: bool
    _bank: bool
    _mount: bool
    _obstacles: bool

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_i()
        self.maxlen(128)
        self._equipment = False
        self._inventory = False
        self._store = False
        self._bank = False
        self._mount = False
        self._obstacles = False

    def equipment(self, equipment: bool = True):
        self._equipment = equipment
        return self

    def inventory(self, inventory: bool = True):
        self._inventory = inventory
        return self

    def store(self, store: bool = True):
        self._store = store
        return self

    def bank(self, bank: bool = True):
        self._bank = bank
        return self

    def mount(self, mount: bool = True):
        self._mount = mount
        return self

    def obstacles(self, obstacles: bool = True):
        self._obstacles = obstacles
        return self

    def get_store(self) -> Store:
        return self.get_location()

    def to_value(self, val: str):
        if not val:
            return None
        p = self.get_player()
        val = val.lower()

        m = re.match(r"^(\d+)x(.*)$", val)
        if m: val = m.group(2)
        candidates = []
        if self._equipment:
            for slot in GDT_Slot.SLOTS:
                if slot[2:4] == val: # 2 letter shortcut for #ex ar/we/bo/he
                    return p.gdo_value(slot)
                if item := p.get_equipment(slot):
                    if val in item.render_name().lower():
                        candidates.append(item)
        if self._inventory:
            if val.isdigit():
                val = int(val)
                if val < 1 or val > len(p.inventory):
                    raise ShadowdogsException('err_list_number', (len(p.inventory),))
                return p.inventory[int(val) - 1]
            candidates.extend(p.inventory.get_by_abbrev(val))
        if self._bank:
            if val.isdigit():
                val = int(val)
                if val < 1 or val > len(p.bank):
                    raise ShadowdogsException('err_list_number', (len(p.inventory),))
                return p.bank[int(val) - 1]
            candidates.extend(p.bank.get_by_abbrev(val))
        if self._store:
            store = self.get_store()
            items = store.get_shop_items(self.get_player())
            return items.get_item_by_arg(val)
        if self._mount:
            candidates.extend(p.mount.get_by_abbrev(val))
        if self.obstacles:
            for obstacle in self.get_location().obstacles(p.get_party().get_action_name(), p):
                if val in obstacle.render_name().lower():
                    candidates.append(obstacle)
                if val == obstacle.render_name().lower():
                    return obstacle
        if len(candidates) == 1:
            return candidates[0]
        elif len(candidates) > 1:
            raise ShadowdogsException('err_item_name_ambiguous', (candidates.__str__(),))
        return None

    def validate(self, val: str|None) -> bool:
        if value := self.get_value():
            return True
        if self._not_null:
            return self.error('err_sd_unknown_item')
        return True
