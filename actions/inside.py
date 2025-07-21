from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party

class inside(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        from gdo.shadowdogs.engine.World import World
        return World.get_location(target_string)

    async def on_start(self, party: 'SD_Party'):
        pass

    async def on_completed(self, party: 'SD_Party'):
        pass
