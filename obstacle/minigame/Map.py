from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.obstacle.minigame.tile.OOB import OOB
from gdo.shadowdogs.obstacle.minigame.tile.Tile import Tile



class Map(WithShadowFunc):

    _x: int
    _y: int
    _w: int
    _h: int
    _r: int # random seed
    _tiles: list[Tile]

    XD = {
        'n': 0,
        'r': 1,
        'd': 0,
        'l': -1,
        'u': 0,
    }

    YD = {
        'n': 0,
        'r': 0,
        'd': 1,
        'l': 0,
        'u': -1,
    }

    def __init__(self, w: int, h: int, r: int = 0):
        super().__init__()
        self._w = w
        self._h = h
        self._r = r
        self._tiles = []

    def get_x(self, direction: str = 'n') -> int:
        return self._x + Map.XD.get(direction)

    def get_y(self, direction: str = 'n') -> int:
        return self._y + Map.YD.get(direction)

    def get_tile(self, x: int, y: int) -> Tile:
        try:
            return self._tiles[y * self._w + x]
        except IndexError:
            return OOB()

    def get_tile_for(self, direction: str) -> Tile:
        return self.get_tile(self.get_x(direction), self.get_y(direction))
