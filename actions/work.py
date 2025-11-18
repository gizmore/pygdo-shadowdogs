from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class work(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        return self.world().get_location(target_string)

    async def on_start(self, party: 'SD_Party'):
        pass

    async def execute(self, party: 'SD_Party'):
        pass

    async def on_completed(self, party: 'SD_Party'):
        await party.resume()
        await self.get_target(party, party.get_target_string()).on_work_over()
