from gdo.shadowdogs.city.y2064.Nauen.locations.forest.Forest import Forest
from gdo.shadowdogs.city.y2064.Nauen.locations.paulinaue.Paulinaue import Paulinaue
from gdo.shadowdogs.city.y2064.Nauen.locations.TrainStation import TrainStation
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Nauen(City):

    MIN_LEVEL = 4

    Forest: Forest = Forest()
    Paulinaue: Paulinaue = Paulinaue()
    TrainStation: TrainStation = TrainStation()

    LOCATIONS: list[Location] = [
        Forest,
        Paulinaue,
        TrainStation,
    ]

