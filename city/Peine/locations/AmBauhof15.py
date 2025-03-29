from gdo.shadowdogs.locations.Exit import Exit
from gdo.shadowdogs.locations.Location import Location


class AmBauhof15(Exit):

    def sd_exit_to(self) -> Location:
        from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
        return Shadowdogs.AmBauhof15.Stairs
