from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

from gdo.shadowdogs.locations.City import City

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party

class outside(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        if target_string.count('.') == 2:
            return self.world().get_location(target_string)
        else:
            return self.world().get_city(target_string)

    async def on_start(self, party: 'SD_Party'):
        await self.send_to_party(party, self.get_action_text_key(party), self.get_action_text_args(party))
        location = self.get_location()
        if not isinstance(location, City):
            await self.give_party_kp(party, location)
            await location.sd_on_exited()
