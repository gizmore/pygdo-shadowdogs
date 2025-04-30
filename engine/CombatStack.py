from gdo.base.Method import Method
from gdo.base.Util import Random
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.method.attack import attack

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class CombatStack(WithShadowFunc):

    command: MethodSD|None
    eta: int
    player: 'SD_Player'

    def __init__(self, player: 'SD_Player'):
        self.player = player
        self.reset()

    def reset(self):
        self.command = None # self.get_default_command()
        qui = self.player.g('p_qui')
        fig = self.player.g('p_fig')
        self.eta = self.get_time() + Random.mrand(2, max(Shadowdogs.SECONDS_INITIATIVE // (((1 + qui + fig) // 2) + 1), 8))

    def get_default_command(self) -> MethodSD:
        user = self.player.get_user()
        return (attack().env_user(user, True).
                env_server(user.get_server()))

    async def tick(self):
        t = self.get_time()
        if t > self.eta:
            self.eta = t + await self.execute()
            self.command = None #  'sdattack'

    async def execute(self):
        if self.command is None:
            self.command = self.get_default_command()
        gdt = await self.command.execute()
        return self.command.sd_combat_seconds()


