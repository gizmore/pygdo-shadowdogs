from typing import Type

from gdo.base.GDT import GDT
from gdo.shadowdogs.GDT_Direction import GDT_Direction
from gdo.shadowdogs.engine.MethodSDHack import MethodSDHack
from gdo.shadowdogs.item.classes.hack.Executable import Executable
from gdo.shadowdogs.item.classes.hack.exe.Ping import Ping
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.minigame.tile.OOB import OOB
from gdo.shadowdogs.obstacle.minigame.tile.Tile import Tile


class xping(MethodSDHack):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdping'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdping'

    def sd_requires_item_klass(self) -> list[str]:
        return ['Ping']

    def sd_executable_type(self) -> Type[Executable]:
        return Ping

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
        if type(tile) is OOB:
            await self.send_to_player(player, 'msg_sd_hack_ping_oob')
            map.set_visible(direction, Tile.OOB)
        await self.send_to_player(player, 'msg_sd_hack_ping_land')
