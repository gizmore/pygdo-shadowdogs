from gdo.shadowdogs.locations.Exit import Exit
from gdo.shadowdogs.locations.Location import Location


class Stairs(Exit):

    def sd_exit_to(self) -> Location:
        from gdo.shadowdogs.engine.World import World
        return World.Peine.AmBauhof15
