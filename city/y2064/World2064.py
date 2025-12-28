from gdo.shadowdogs.city.y2064.Nauen.Nauen import Nauen
from gdo.shadowdogs.city.y2064.Oberg.Oberg import Oberg
from gdo.shadowdogs.city.y2064.Peine.Peine import Peine
from gdo.shadowdogs.city.y2064.PoliceStation.PoliceStation import PoliceStation
from gdo.shadowdogs.engine.WorldBase import WorldBase
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.city.y2064.Brunswick.Brunswick import Brunswick

class World2064(WorldBase):

    MIN_LEVEL = 2

    Brunswick: Brunswick = Brunswick()
    Nauen: Nauen = Nauen()
    Oberg: Oberg = Oberg()
    Peine: Peine = Peine()
    PoliceStation: PoliceStation = PoliceStation()

    CITIES: dict[str, City] = {
        'Brunswick': Brunswick,
        'Nauen': Nauen,
        'Oberg': Oberg,
        'Peine': Peine,
        'PoliceStation': PoliceStation,
    }
