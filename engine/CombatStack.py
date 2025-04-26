from gdo.base.Util import Random
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.method.attack import attack

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class CombatStack(WithShadowFunc):

    command: str
    eta: int
    player: 'SD_Player'

    def __init__(self, player: 'SD_Player'):
        self.player = player
        self.reset()

    def reset(self):
        self.command = 'sdattack'
        qui = self.player.g('p_qui')
        fig = self.player.g('p_fig')
        self.eta = self.get_time() + Random.mrand(2, max(Shadowdogs.SECONDS_INITIATIVE // (((1 + qui + fig) // 2) + 1), 8))

    async def tick(self):
        t = self.get_time()
        if t > self.eta:
            self.eta = t + await self.execute()
            self.command = 'sdattack'

    async def execute(self):
        parts = self.command.split(" ")
        method = self.get_method(parts[0]) or attack()
        method.player(self.player)
        method.env_user(self.player.get_user(), True)
        method.env_server(self.player.get_user().get_server())
        method._raw_args.add_cli_line(parts[1:])
        gdt = await method.execute()
        return method.sd_combat_seconds()


