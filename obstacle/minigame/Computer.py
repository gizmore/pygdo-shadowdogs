from gdo.base.GDT import GDT
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.minigame.tile.Tile import Tile

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.obstacle.minigame.Map import Map


class Computer(Obstacle):

    _width: int
    _height: int

    _maps: dict[SD_Player, 'Map']
    _tiles: list[Tile]

    # _sinks: int
    # _traps: list[int]
    # _vaults: list[tuple[str,int,str,int]]

    def __init__(self, name: str = None):
        super().__init__(name)
        self._width = 3
        self._height = 3
        self._maps = {}
        self._tiles = []
        # self._sinks = 0
        # self._vaults = []
        # self._traps = []

    def tile(self, tile: Tile):
        self._tiles.append(tile)
        return self

    def sd_commands(self) -> list[str]:
        return [
            'sdhack',
        ]

    def width(self, width: int):
        self._width = width
        return self

    def height(self, height: int):
        self._height = height
        return self

    def get_map(self, player: SD_Player) -> 'Map':
        from gdo.shadowdogs.obstacle.minigame.Gen import Gen
        if player in self._maps:
            return self._maps.get(player)
        map = Gen().player(player).generate(self)
        self._maps[player] = map
        return map

    async def on_hack(self, params: list[GDT]):
        pa = self.get_party()
        await pa.do(Action.HACK, self.__class__.__name__)
