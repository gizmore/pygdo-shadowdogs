from gdo.shadowdogs.city.Peine.locations.AmBauhof15 import AmBauhof15
from gdo.shadowdogs.city.Peine.locations.Kief import Kief
from gdo.shadowdogs.city.Peine.locations.Park import Park
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Peine(City):

    AmBauhof15: AmBauhof15 = AmBauhof15()
    Park: Park = Park()
    WeaponSmith: Kief = Kief()

    LOCATIONS: list[Location] = [
        AmBauhof15,
        Park,
        Kief,
    ]
