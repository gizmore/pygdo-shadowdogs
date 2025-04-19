from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.World import World

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party

class inside(Action):

    def get_target(self, party: 'SD_Party'):
        return World.get_location(party.get_target_string())
