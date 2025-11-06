from gdo.shadowdogs.locations.Exit import Entry
from gdo.shadowdogs.locations.Location import Location


class Police(Entry):

    def sd_exit_to(self) -> Location:
        raise self.world().World2064.PoliceStationStationShadowdogsException('err_sd_stub')
