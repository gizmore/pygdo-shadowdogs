from gdo.core.GDT_String import GDT_String

from typing import TYPE_CHECKING

from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class GDT_ItemArg(GDT_String):

    _equipment: bool
    _inventory: bool
    _store: bool
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

    def mount(self, mount: bool = True):
        self._mount = mount
        return self

    def obstacles(self, obstacles: bool = True):
        self._obstacles = obstacles
        return self

    def get_player(self) -> 'SD_Player':
        return self._gdo

    def to_value(self, val: str):
        p = self.get_player()
        val = val.lower()
        if self._equipment:
            candidates = []
            for slot in GDT_Slot.SLOTS:
                if slot[2:4] == val[0:2]:
                    return p.gdo_value(slot)
                if item := p.get_equip(slot):
                    if item.render_name().lower().index(val) >= 0:
                        candidates.append(item)
            if len(candidates) == 1:
                return candidates[0]
            elif len(candidates) > 1:
                raise ShadowdogsException('err_item_name_ambiguous')
        if self._inventory:
            if val[0].isdigit():
                return p.inventory[int(val) - 1]
            return p.inventory.get_by_abbrev(val)

