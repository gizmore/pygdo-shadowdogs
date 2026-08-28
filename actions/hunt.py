from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class hunt(Action):
    """Follow a player and resolve their position when the hunt ends."""

    def get_target(self, party: 'SD_Party', target_string: str) -> SD_Player | None:
        return SD_Player.table().get_by_aid(target_string)

    async def on_start(self, party: 'SD_Party'):
        await self.send_to_party(party, self.get_action_text_key(party), self.get_action_text_args(party))

    async def execute(self, party: 'SD_Party'):
        return

    async def on_completed(self, party: 'SD_Party'):
        target = self.get_target(party, party.get_target_string())
        location = target.get_party().get_location() if target else None
        if location and target.get_city() is party.get_city():
            await party.do(Action.OUTSIDE, location.get_location_key())
            if target.get_party().does(Action.OUTSIDE):
                await self.send_to_party(party, 'msg_sd_hunt_found', (target.render_name(), location.render_name()))
        else:
            await party.do(Action.OUTSIDE, party.get_last_target_string())
            await self.send_to_party(party, 'err_sd_hunt_lost', (target.render_name() if target else '?',))
        await super().on_completed(party)
