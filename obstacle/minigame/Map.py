from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.obstacle.minigame.tile.Tile import Tile



class Map(WithShadowFunc):

    _w: int
    _h: int
    _r: int
    _tiles: list[Tile]

    def __init__(self, w: int, h: int, r: int = 0):
        super().__init__()
        self._w = w
        self._h = h
        self._r = r
        self._tiles = []

    def get_tile(self, x: int, y: int) -> Tile:
        return self._tiles[y * self._w + x]

    def get_tile_for(self, ):
        pass
