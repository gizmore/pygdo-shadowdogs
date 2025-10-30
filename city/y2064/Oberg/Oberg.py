from gdo.shadowdogs.city.y2064.Oberg.locations.grandma.Grandma import Grandma
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Oberg(City):

    Grandma: Grandma = Grandma()

    LOCATIONS: list[Location] = [
        Grandma
    ]
