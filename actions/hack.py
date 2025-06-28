from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

from gdo.shadowdogs.obstacle.Obstacle import Obstacle

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class hack(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        return Obstacle.get_by_obstacle_id(target_string)
