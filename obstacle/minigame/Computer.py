from gdo.base.Util import Random
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.ui.WithSize import WithSize


class Computer(WithSize, Obstacle):

    _width: int
    _height: int

    def width(self, width: int):
        self._width = width
        return self

    def height(self, height: int):
        self._height = height
        return self

    def __init__(self, name: str):
        super().__init__(name)
        self._width = 3
        self._height = 3


    def on_hack(self):
        pass


