from gdo.shadowdogs.city.y2064.Nauen.locations.paulinchen.Paulinchen import Paulinchen
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Nauen(City):

    Paulinchen: Paulinchen = Paulinchen(),

    LOCATIONS: list[Location] = [
        Paulinchen,
    ]

