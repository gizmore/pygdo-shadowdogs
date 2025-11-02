from gdo.shadowdogs.city.y2064.Marketplace.Marketplace import Marketplace
from gdo.shadowdogs.city.y2064.Peine.Peine import Peine
from gdo.shadowdogs.city.y2064.Oberg.Oberg import Oberg
from gdo.shadowdogs.city.y2064.PoliceStation.PoliceStation import PoliceStation
from gdo.shadowdogs.engine.WorldBase import WorldBase
from gdo.shadowdogs.locations.City import City


class World2064(WorldBase):

    Peine: Peine = Peine()
    Oberg: Oberg = Oberg()
    Marketplace: Marketplace = Marketplace()
    PoliceStation: PoliceStation = PoliceStation()

    CITIES: dict[str, City] = {
        'Peine': Peine,
        'PoliceStation': PoliceStation,
        'Marketplace': Marketplace,
    }
