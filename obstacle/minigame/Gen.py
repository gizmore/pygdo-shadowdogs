from gdo.base.Util import Random
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.WithProbability import WithProbability
from gdo.shadowdogs.obstacle.minigame.Computer import Computer
from gdo.shadowdogs.obstacle.minigame.Map import Map
from gdo.shadowdogs.obstacle.minigame.tile.Empty import Empty


class Gen(WithShadowFunc):

    def generate(self, computer: Computer) -> Map:
        p = self.get_player()
        w = computer._width
        h = computer._height
        seed = int(p.gb('p_seed'))
        scramble = computer.gobs('scrambled') or 0
        map: Map = Map(w, h, seed + scramble)
        probable_tiles = [
            (Empty, )
        ]

        for y in range(h):
            map.set_tile(0, y, Empty().player(self.get_player()))



        with Random(int(p.gb('p_seed')) + int(scramble)):
            for y in range(h):
                for x in range(w-1):



