from gdo.shadowdogs.city.Peine.locations.AmBauhof15 import AmBauhof15
from gdo.shadowdogs.city.Peine.locations.Park import Park
from gdo.shadowdogs.city.Peine.locations.WeaponSmith import WeaponSmith
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Peine(City):

    AmBauhof15: AmBauhof15 = AmBauhof15()
    Park: Park = Park()
    WeaponSmith: WeaponSmith = WeaponSmith()

    LOCATIONS: list[Location] = [
        AmBauhof15,
        Park,
        WeaponSmith,
    ]
