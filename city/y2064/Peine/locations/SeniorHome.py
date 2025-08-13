from gdo.shadowdogs.city.y2064.SeniorsHome.locations.Exit import Exit
from gdo.shadowdogs.locations.Exit import Entry
from gdo.shadowdogs.locations.Location import Location


class SeniorHome(Entry):

    def sd_exit_to(self) -> Location:
        return Exit
