from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class fight(Action):

    def get_target(self, party: 'SD_Party'):
        return Shadowdogs.PARTIES.get(party.get_target_string())

    def get_enemy_party(self) -> 'SD_Party':
        return self.get_party().get_target_party()

    async def on_start(self, party: 'SD_Party'):
        epa = self.get_enemy_party()
        await self.send_to_party(epa, 'msg_sd_fight_started', (party.render_members(),))
        await self.send_to_party(party, 'msg_sd_fight_started', (epa.render_members(),))

    async def execute(self, party: 'SD_Party'):
        for player in party.members:
            await player.combat_tick()
