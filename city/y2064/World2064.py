from gdo.shadowdogs.city.y2064.Nauen.Nauen import Nauen
from gdo.shadowdogs.city.y2064.Oberg.Oberg import Oberg
from gdo.shadowdogs.city.y2064.Peine.Peine import Peine
from gdo.shadowdogs.city.y2064.PoliceStation.PoliceStation import PoliceStation
from gdo.shadowdogs.engine.WorldBase import WorldBase
from gdo.shadowdogs.locations.City import City


class World2064(WorldBase):

    MIN_LEVEL = 2

    Nauen: Nauen = Nauen()
    Oberg: Oberg = Oberg()
    Peine: Peine = Peine()
    PoliceStation: PoliceStation = PoliceStation()

    CITIES: dict[str, City] = {
        'Nauen': Nauen,
        'Oberg': Oberg,
        'Peine': Peine,
        'PoliceStation': PoliceStation,
    }
