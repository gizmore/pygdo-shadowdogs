from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations import Exit
from gdo.shadowdogs.locations.Location import Location


class Stairs(Exit):

    def sd_exit_to(self) -> Location:
        return Shadowdogs.Peine.AmBauhof15
