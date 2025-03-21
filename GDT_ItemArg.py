from gdo.core.GDT_ObjectSelect import GDT_ObjectSelect


class GDT_ItemArg(GDT_ObjectSelect):

    _inventory: bool
    _equipment: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._equipment = False
        self._inventory = False

    def inventory(self, inventory: bool = True):
        self._inventory = inventory
        return self

    def equipment(self, equipment: bool = True):
        self._equipment = equipment
        return self
