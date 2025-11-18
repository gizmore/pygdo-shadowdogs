from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.locations.Location import Location


class Exit(Location):

    async def on_entered(self):
        await super().on_entered()
        await self.get_party().do(self.sd_exit_action(), self.sd_exit_to().get_location_key())

    def sd_exit_to(self) -> Location:
        raise ShadowdogsException('err_sd_stub')

    def sd_exit_action(self) -> str:
        return Action.OUTSIDE


class Entry(Exit):

    def sd_exit_action(self) -> str:
        return Action.INSIDE
