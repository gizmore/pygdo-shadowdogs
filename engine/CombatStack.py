from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player


class CombatStack(WithShadowFunc):

    command: str
    eta: int
    player: 'GDO_Player'

    def __init__(self, player: 'GDO_Player'):
        self.player = player
        self.reset()

    def reset(self):
        self.command = 'sdattack'
        self.eta = 0

    def tick(self):
        t = self.mod_sd().cfg_time()
        if t > self.eta:
            self.eta = t + self.execute()
            self.command = 'sdattack'

    def execute(self):
        parts = self.command.split()
        method = self.get_method(parts[0])
        method.env_user(self.player.get_user())
        method.env_server(self.player.get_user().get_server())
        method._raw_args.add_cli_line(parts[1:]).execute()
        return method.sd_combat_seconds()


