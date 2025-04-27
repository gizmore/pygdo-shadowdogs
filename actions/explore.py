from gdo.shadowdogs.actions.Action import Action


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class explore(Action):

    def get_target(self, party: 'SD_Party'):
        from gdo.shadowdogs.engine.World import World
        return getattr(World, party.get_target_string())

    async def on_start(self, party: 'SD_Party'):
        await self.send_to_party(party, self.get_action_text_key(party), self.get_action_text_args(party))
