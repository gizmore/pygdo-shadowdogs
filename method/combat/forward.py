from functools import partial

from gdo.base.Application import Application
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class forward(MethodSD):

    def sd_requires_action(self) -> list[str]|None:
        return [
            'fight',
        ]

    def sd_combat_seconds(self) -> int:
        return Shadowdogs.SECONDS_PER_METER * Shadowdogs.METERS_PER_FORWARD

    async def sd_before_execute(self):
        player = self.get_player()
        Application.EVENTS.add_timer_async(Shadowdogs.SECONDS_PER_METER, partial(self.forward, player), Shadowdogs.METERS_PER_FORWARD)
        await self.send_to_player(player, 'msg_sd_forward', (Shadowdogs.METERS_PER_FORWARD, player.render_busy()))

    async def forward(self, player: SD_Player):
        party = player.get_party()
        sign = party.combat_diraction_sign()
        player.distance += sign * Shadowdogs.METERS_PER_FORWARD
