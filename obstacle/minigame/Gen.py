from gdo.base.Util import Random
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.obstacle.minigame.Computer import Computer
from gdo.shadowdogs.obstacle.minigame.Map import Map


class Gen(WithShadowFunc):

    def generate(self, computer: Computer) -> Map:
        p = self.get_player()
        scramble = computer.gobs('scrambled') or 0
        with Random(int(p.gb('p_seed')) + int(scramble)):
            pass
