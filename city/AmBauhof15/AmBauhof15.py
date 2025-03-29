from gdo.shadowdogs.city.AmBauhof15.locations.Etage2Left import Etage2Left
from gdo.shadowdogs.city.AmBauhof15.locations.Kitchen import Kitchen
from gdo.shadowdogs.city.AmBauhof15.locations.Stairs import Stairs
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class AmBauhof15(City):

    Stairs: Stairs = Stairs()
    Kitchen: Kitchen = Kitchen()
    Etage2Left: Etage2Left = Etage2Left()

    LOCATIONS: list[Location] = {
        Stairs,
        Kitchen,
        Etage2Left,
    }
