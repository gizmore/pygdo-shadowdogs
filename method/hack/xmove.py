from gdo.base.GDT import GDT
from gdo.shadowdogs.GDT_Direction import GDT_Direction
from gdo.shadowdogs.engine.MethodSDHack import MethodSDHack
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class xmove(MethodSDHack):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdmove'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdmov'

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Direction('direction').not_null(),
        ]

    async def execute_obstacle(self, obstacle: Obstacle):
        player = self.get_player()
        computer = self.get_computer()
        map = computer.get_map(player)
        direction = self.param_val('direction')
        tile = map.get_tile_for(direction)
        await tile.visit()

