from gdo.shadowdogs.locations.Exit import Entry
from gdo.shadowdogs.locations.Location import Location


class Marketplace(Entry):

    def sd_exit_to(self) -> Location:
        from gdo.shadowdogs.city.y2064.World2064 import World2064
        return World2064.Marketplace.Entrance
