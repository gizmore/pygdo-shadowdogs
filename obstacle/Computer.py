from gdo.base.Util import Random
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO
from gdo.shadowdogs.engine.WithProbability import WithProbability
from gdo.shadowdogs.obstacle.Obstacle import Obstacle

# c1
#...
#P.$
#...

# 1)

class Tile(WithProbability):
    probability: int = 100

class Ice(Tile):
    probability: int = 60
    power: int
    def __init__(self):
        super().__init__()
        self.power = Random.mrand(1, 5)

class Exit(Tile):
    probability: int = 100

class Wall(Tile):
    probability: int = 100

class Disconnect(Tile):
    probability: int = 20

class Passage(Tile):
    probability: int = 100

class Trap(Tile):
    probability: int = 40


class Map(WithPlayerGDO):

    TILES: list[WithProbability] = [
        Ice,
        Exit,
        Wall,
        Disconnect,
        Passage,
        Trap,
    ]

    w: int
    h: int
    map: list[Tile]

    def __init__(self, w: int = 33, h: int = 3):
        self.w = w
        self.h = h
        self.map = []

    def tile_at(self, x: int, y: int):
        return self.map[y * self.w + x]

    def random(self):
        for y in range(self.h):
            for x in range(self.w):
                self.map.append(WithProbability.probable_item(self.TILES)())

class Computer(Obstacle):

    maps: dict[SD_Player, Map]

    def __init__(self, name: str):
        super().__init__(name)
        self.maps = {}

    def random_map(self):
        map = Map(32,3)
        map.player(self._player)
        map.random()

    def get_map(self):
        return self.maps[self.get_player()]
