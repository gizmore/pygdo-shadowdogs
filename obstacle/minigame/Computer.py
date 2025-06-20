from gdo.base.Util import Random
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Computer(Obstacle):

    _width: int
    _height: int

    def width(self, w: int):
        return self

    def on_hack(self):
        p = self.get_player()

        with Random(p.gb('p_seed')):
