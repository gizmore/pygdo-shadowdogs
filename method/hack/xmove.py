from typing import Type

from gdo.base.GDT import GDT
from gdo.shadowdogs.GDT_Direction import GDT_Direction
from gdo.shadowdogs.engine.MethodSDHack import MethodSDHack
from gdo.shadowdogs.item.classes.hack.Executable import Executable
from gdo.shadowdogs.item.classes.hack.exe.Move import Move
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class xmove(MethodSDHack):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdmove'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdmov'

    def sd_requires_item_klass(self) -> list[str]:
        return [
            'Move',
        ]

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Direction('direction').diagonal(self.get_executable_level() >= 2).not_null(),
        ]

    def sd_executable_type(self) -> Type[Executable]:
        return Move

    def get_executable_level(self) -> int:
        level = 0
        for item in self.get_player().all_programs():
            if isinstance(item, self.sd_executable_type()):
                l = item.g('level')
                if l > level:
                    level = l
        return level

    async def execute_obstacle(self, obstacle: Obstacle):
        player = self.get_player()
        computer = self.get_computer()
        map = computer.get_map(player)
        direction = self.param_val('direction')
        tile = map.get_tile_for(direction)
        await tile.visit()
        return self.empty()
