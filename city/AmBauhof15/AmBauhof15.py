from gdo.shadowdogs.city.AmBauhof15.locations.Etage2Left import Etage2Left
from gdo.shadowdogs.city.AmBauhof15.locations.Stairs import Stairs
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class AmBauhof15(City):

    Stairs: Stairs = Stairs()
    Kitchen: Stairs = Stairs()

    LOCATIONS: list[Location] = [
        Stairs,
        Etage2Left(),
    ]
