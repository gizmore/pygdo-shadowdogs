from gdo.shadowdogs.city.y2064.Peine.locations.AmBauhof15 import AmBauhof15
from gdo.shadowdogs.city.y2064.Peine.locations.Marketplace import Marketplace
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Peine(City):

    AmBauhof15: AmBauhof15 = AmBauhof15()
    Marketplace: Marketplace = Marketplace()

    LOCATIONS: list[Location] = [
        AmBauhof15,
        Marketplace,
    ]
