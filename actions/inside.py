from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party

class inside(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        return self.world().get_location(target_string)

    async def on_start(self, party: 'SD_Party'):
        for member in party.members:
            await member.give_kp(member, self.get_location())
        await self.get_location().sd_on_entered()

    async def on_completed(self, party: 'SD_Party'):
        pass
