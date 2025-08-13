from gdo.shadowdogs.city.y2064.Marketplace.Marketplace import Marketplace
from gdo.shadowdogs.city.y2064.Peine.Peine import Peine
from gdo.shadowdogs.engine.WorldBase import WorldBase
from gdo.shadowdogs.locations.City import City


class World2064(WorldBase):

    Peine: Peine = Peine()
    Marketplace: Marketplace = Marketplace()

    CITIES: dict[str, City] = {
        'Peine': Peine,
        'Marketplace': Marketplace,
    }
