from gdo.shadowdogs.city.y2064.Marketplace.locations.Entrance import Entrance
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Marketplace(City):

    Entrance: Entrance = Entrance()

    LOCATIONS: list[Location] = [
        Entrance,
    ]

