from gdo.shadowdogs.city.y2064.Bothel.locations.gruendel.Gruendel import Gruendel
from gdo.shadowdogs.city.y2064.Bothel.locations.klawitter.Klawitter import Klawitter
from gdo.shadowdogs.city.y2064.Bothel.locations.winkelmann.Winkelmann import Winkelmann
from gdo.shadowdogs.city.y2064.Bothel.locations.samland.Samland import Samland
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Bothel(City):

    Gruendel: Gruendel = Gruendel()
    Klawitter: Klawitter = Klawitter()
    Samland: Samland = Samland()
    Winkelmann: Winkelmann = Winkelmann()

    LOCATIONS: list[Location] = [
        Gruendel,
        Klawitter,
        Samland,
        Winkelmann,
    ]
