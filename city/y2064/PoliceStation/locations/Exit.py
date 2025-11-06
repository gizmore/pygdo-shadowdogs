from gdo.shadowdogs.locations.Exit import Exit
from gdo.shadowdogs.locations.Location import Location


class Exit(Exit):
    def sd_exit_to(self) -> Location:
        self.world().World2064.Peine.Police