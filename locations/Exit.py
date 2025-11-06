from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.locations.Location import Location


class Exit(Location):

    async def on_entered(self):
        await self.get_party().do(Action.INSIDE)

        await self.send_to_party(self.get_party(), 'msg_sd_entered', (self.get_location().render_name(),))

    def sd_location_actions(self) -> tuple[str]:
        return (self.get_party().get_action_name(),)

    def sd_exit_to(self) -> Location:
        raise ShadowdogsException('err_sd_stub')

    def sd_exit_action(self) -> str:
        return Action.OUTSIDE


class Entry(Exit):

    def sd_exit_action(self) -> str:
        return Action.INSIDE
