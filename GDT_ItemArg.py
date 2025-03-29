from gdo.core.GDT_Select import GDT_Select


class GDT_ItemArg(GDT_Select):

    _inventory: bool
    _equipment: bool
    _store: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._equipment = False
        self._inventory = False
        self._store = False

    def inventory(self, inventory: bool = True):
        self._inventory = inventory
        return self

    def equipment(self, equipment: bool = True):
        self._equipment = equipment
        return self

    def store(self, store: bool = True):
        self._store = store
        return self

    def gdo_choices(self) -> dict:
        return {

        }
