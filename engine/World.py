from gdo.shadowdogs.city.Peine.Peine import Peine
from gdo.shadowdogs.city.AmBauhof15.AmBauhof15 import AmBauhof15
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City


class World:
    Peine: Peine = Peine()
    AmBauhof15: AmBauhof15 = AmBauhof15()
    CITIES: dict[str,'City'] = {
        'peine': Peine,
        'ambauhof15': AmBauhof15,
    }
