from gdo.shadowdogs.city.y2064.Peine.locations.SeniorsHome.locations.Entrance import Entrance
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Exit import Exit
from gdo.shadowdogs.locations.Location import Location


class SeniorHome(City, Exit):

    def sd_exit_to(self) -> Location:
        return Entrance
