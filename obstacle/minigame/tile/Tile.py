from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.obstacle.minigame.Map import Map


class Tile(WithShadowFunc):

    HIDDEN = 0
    OOB = 1
    NOT_OOB = 1
    VISIBLE = 3

    visibility: int
    visited: bool
    _map: 'Map'

    def __init__(self) -> None:
        super().__init__()
        self.visibility = self.HIDDEN
        self.visited = False

    async def visit(self):
        self.visited = True
        self.visibility = self.VISIBLE
        return self

    def map(self, map: 'Map'):
        self._map = map
        return self

    def disconnect(self):
        self._map,disconnect()
