from gdo.shadowdogs.city.y2064.Oberg.locations import BusStop
from gdo.shadowdogs.city.y2064.Oberg.locations.grandma.Grandma import Grandma
from gdo.shadowdogs.city.y2064.Oberg.locations.BusStop import BusStop
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Oberg(City):

    Grandma: Grandma = Grandma()
    BusStop: BusStop = BusStop()

    LOCATIONS: list[Location] = [
        Grandma,
        BusStop,
    ]
