from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party

class outside(Action):

    def get_target(self, party: 'SD_Party'):
        from gdo.shadowdogs.engine.World import World
        return World.get_location(party.get_target_string())
