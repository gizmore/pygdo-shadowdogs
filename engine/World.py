from gdo.base.Util import Strings
from gdo.shadowdogs.city.Peine.Peine import Peine
from gdo.shadowdogs.city.AmBauhof15.AmBauhof15 import AmBauhof15
from typing import TYPE_CHECKING

from gdo.shadowdogs.locations.Location import Location

if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City


class World:

    Peine: Peine = Peine()
    AmBauhof15: AmBauhof15 = AmBauhof15()

    CITIES: dict[str,'City'] = {
        'peine': Peine,
        'ambauhof15': AmBauhof15,
    }

    @classmethod
    def get_city(cls, loc_str: str) -> 'City':
        return cls.CITIES.get(Strings.substr_to(loc_str, '.', loc_str).lower())

    @classmethod
    def get_location(cls, loc_str: str) -> 'Location':
        city_name, loc_name = loc_str.split('.')
        city = cls.get_city(city_name)
        return getattr(city, loc_name)
