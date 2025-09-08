from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class goto(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        return self.world().get_location(target_string)

    async def on_start(self, party: 'SD_Party'):
        await self.send_to_party(party, self.get_action_text_key(party), self.get_action_text_args(party, 'start'))

    async def execute(self, party: 'SD_Party'):
        await self.get_city().on_explore(party)

    async def on_completed(self, party: 'SD_Party'):
        await self.send_to_party(party, self.get_action_text_key(party, 'was'), self.get_action_text_args(party, 'was'))
        await party.do(Action.INSIDE, party.get_target_string())
