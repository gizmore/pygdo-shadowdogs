from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Computer(Obstacle):

    _width: int
    _height: int

    def width(self, w: int):
        return self

    def on_hack(self):

