from gdo.shadowdogs.locations.Exit import Entry
from gdo.shadowdogs.locations.Location import Location


class Police(Entry):

    def sd_exit_to(self) -> Location:
        raise self.world().World2064.PoliceStationStationShadowdogsException('err_sd_stub')

    async def on_entered(self):
        await self.get_party().do(Action.INSIDE)
        await self.send_to_party(self.get_party(), 'msg_sd_entered', (self.get_location().render_name(),))
