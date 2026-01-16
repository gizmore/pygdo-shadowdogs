from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class fight(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        return Shadowdogs.PARTIES.get(target_string)

    def get_enemy_party(self) -> 'SD_Party':
        return self.get_party().get_target_party()

    def get_action_text_args(self, party: 'SD_Party', scope: str = 'start') -> None|tuple[Any,...]:
        return party.render_members(), party.get_enemy_party().render_members()

    async def on_start(self, party: 'SD_Party'):
        epa = self.get_enemy_party()
        await self.send_to_party(epa, 'msg_sd_fight_started', (party.render_members(),))
        await self.send_to_party(party, 'msg_sd_fight_started', (epa.render_members(),))

    async def on_completed(self, party: 'SD_Party'):
        if not (ep := party.get_target_party()) or ep.is_empty():
            await party.resume()
        else:
            for player in party.members:
                await player.combat_tick()
