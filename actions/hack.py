from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

from gdo.shadowdogs.obstacle.Obstacle import Obstacle

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class hack(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        return Obstacle.get_by_obstacle_id(target_string)

    async def on_start(self, party: 'SD_Party'):
        await self.send_to_party(party, self.get_action_text_key(party), self.get_action_text_args(party))
