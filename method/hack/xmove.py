from gdo.base.GDT import GDT
from gdo.shadowdogs.GDT_Direction import GDT_Direction
from gdo.shadowdogs.engine.MethodSDHack import MethodSDHack
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class move(MethodSDHack):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdmove'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdmov'

    def sd_requires_item_name(self) -> [str]:
        return GDT.EMPTY_LIST

    def sd_requires_item_klass(self) -> [str]:
        return GDT.EMPTY_LIST

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Direction('direction').not_null(),
        ]

    def execute_computer(self, obstacle: Obstacle):

