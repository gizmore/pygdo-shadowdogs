from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class GDT_World(WithShadowFunc, GDT_Enum):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._default_current = False

    def default_current(self, enable: bool = True):
        self._default_current = enable
        return self

    def get_val(self):
        val = super().get_val()
        if val is None and self._default_current:
            world = self.get_player().get_party().get_world()
            return world.__class__.__name__[5:]
        return val

    def gdo_choices(self) -> dict:
        World = self.world()
        return {
            'y2064': World.World2064,
            'y2077': World.World2077,
            'y2088': World.World2088,
        }
