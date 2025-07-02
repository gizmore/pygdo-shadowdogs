from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.WithProbability import WithProbability


class Tile(WithShadowFunc):

    HIDDEN = 0
    NOT_OOB = 1
    VISIBLE = 2

    visibility: int
    visited: bool

    def __init__(self) -> None:
        super().__init__()
        self.visibility = self.HIDDEN
        self.visited = False

    async def visit(self):
        self.visited = True
        self.visibility = self.VISIBLE
        return self
