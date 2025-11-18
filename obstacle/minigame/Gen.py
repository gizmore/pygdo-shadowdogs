from gdo.base.Util import Random
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.WithProbability import WithProbability
from gdo.shadowdogs.obstacle.minigame.Computer import Computer
from gdo.shadowdogs.obstacle.minigame.tile.Empty import Empty
from gdo.shadowdogs.obstacle.minigame.tile.Password import Password
from gdo.shadowdogs.obstacle.minigame.tile.Sink import Sink
from gdo.shadowdogs.obstacle.minigame.tile.Trap import Trap
from gdo.shadowdogs.obstacle.minigame.tile.Vault import Vault
from gdo.shadowdogs.obstacle.minigame.tile.Wall import Wall

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.obstacle.minigame.Map import Map


class Gen(WithShadowFunc):

    def generate(self, computer: Computer) -> 'Map':
        from gdo.shadowdogs.obstacle.minigame.Map import Map
        p = self.get_player()
        w = computer._width
        h = computer._height
        seed = int(p.gb('p_seed'))
        scramble = computer.gobs('scrambled') or 0
        map: Map = Map(w, h, seed + scramble)
        probable_tiles = [
            (Empty, 10),
            (Wall, 10),
            (Sink, 10),
            (Trap, 5),
            (Password, 3),
            (Vault, 2),
        ]

        for y in range(h):
            map.set_tile(0, y, Empty().player(self.get_player()))

        with Random(int(p.gb('p_seed')) + int(scramble)):
            for y in range(h):
                for x in range(w-1):
                    klass = WithProbability.probable_item(probable_tiles)
                    map.set_tile(0, y, klass().player(self.get_player()))




