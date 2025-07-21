from gdo.base.Util import Random
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.method.combat.attack import attack

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class CombatStack(WithShadowFunc):

    command: MethodSD|None
    eta: int
    last_target: 'SD_Player|None'

    __slots__ = (
        'command',
        'eta',
        'last_target',
    )

    def __init__(self, player: 'SD_Player'):
        self.command = None
        self.eta = 0
        self.player(player)
        self.last_target = None

    def reset(self):
        self.last_target = None
        self.command = None
        qui = self.get_player().g('p_qui')
        fig = self.get_player().g('p_fig')
        self.eta = (self.get_time() + self.get_busy_seconds() +
                    Random.mrand(2, max(Shadowdogs.SECONDS_INITIATIVE // (((1 + qui + fig) // 2) + 1), 8)))

    def get_default_command(self) -> MethodSD:
        cmd = attack().player(self.get_player()).env_user(self.get_user(), True).env_server(self.get_user().get_server())
        ep = self.get_enemy_party()
        if self.last_target:
            pos = self.last_target.party_pos
        else:
            pos = ep.random_member().party_pos
        return cmd.input('target', str(pos))

    async def tick(self):
        if self.get_time() >= self.eta:
            await self.execute()
            self.command = None

    def busy(self, seconds: int):
        self.eta = self.get_time() + seconds

    async def execute(self):
        if self.command is None:
            self.command = self.get_default_command()
        self.busy(self.command.sd_combat_seconds())
        return await self.command.sd_execute()

    def is_busy(self) -> bool:
        return self.eta > self.get_time()

    def get_busy_seconds(self) -> int:
        return max(self.eta - self.get_time(), 0)
