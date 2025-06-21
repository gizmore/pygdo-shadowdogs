from gdo.base.Util import Random
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.minigame.Map import Map
from gdo.ui.WithSize import WithSize


class Computer(Obstacle):

    _width: int
    _height: int

    _maps: dict[SD_Player, Map]

    def __init__(self, name: str):
        super().__init__(name)
        self._width = 3
        self._height = 3
        self._maps = {}

    def width(self, width: int):
        self._width = width
        return self

    def height(self, height: int):
        self._height = height
        return self

    def on_hack(self):
        pass
