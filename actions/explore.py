from gdo.base.Util import Strings
from gdo.shadowdogs.actions.Action import Action


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class explore(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        return getattr(party.get_world(), Strings.rsubstr_from(target_string, '.'))

    async def on_start(self, party: 'SD_Party'):
        await self.send_to_party(party, self.get_action_text_key(party), self.get_action_text_args(party))

    async def execute(self, party: 'SD_Party'):
        await self.get_city().on_explore(party)

    async def on_completed(self, party: 'SD_Party'):
        await party.get_city().on_explored(party)

