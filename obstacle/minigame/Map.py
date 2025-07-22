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

    OOB: OOB = OOB()

    _visible: list[int]

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
        self._visible = []
        for y in range(h+2):
            for x in range(w+2):
                self._visible[y * (w+2) + x] = 0

    def get_x(self, direction: str = 'n') -> int:
        return self._x + Map.XD.get(direction)

    def get_y(self, direction: str = 'n') -> int:
        return self._y + Map.YD.get(direction)

    def get_tile(self, x: int, y: int) -> Tile:
        try:
            return self._tiles[y * self._w + x].player(self.get_player())
        except IndexError:
            vx = x + 1
            vy = y + 1
            self._visible[x + (self._w+2) * y] = Tile.VISIBLE
            return self.OOB.player(self.get_player())

    def get_tile_for(self, direction: str) -> Tile:
        return self.get_tile(self.get_x(direction), self.get_y(direction))

    def set_visible(self, direction: str, visibility: int):
        x = self.get_x(direction)
        y = self.get_y(direction)
        vx = x + 1
        vy = y + 1
        self._visible[vx + (self._w + 2) * vy] = visibility
        return self
