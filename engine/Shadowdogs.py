from typing import TYPE_CHECKING

from gdo.base.Util import Strings

if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party
    from gdo.shadowdogs.GDO_Player import GDO_Player
    from gdo.shadowdogs.GDO_NPC import GDO_NPC
    from gdo.shadowdogs.locations.Location import Location
    from gdo.shadowdogs.locations.City import City


class Shadowdogs:

    PARTIES: dict[str,'GDO_Party'] = {}
    PLAYERS: dict[str,'GDO_Player'] = {}
    NPCS: dict[str,'GDO_NPC'] = {}


    SECONDS_PER_SECOND = 6
    SECONDS_PER_HP = 5

    MAX_WEIGHT_PER_STRENGTH = 1000
    HP_PER_BODY = 2
    HP_PER_STRENGTH = 1
    HP_PER_LEVEL = 1
    MP_PER_LEVEL = 1
    MP_PER_MAGIC = 3
    MP_PER_INTELLIGENCE = 2
    MP_PER_WISDOM = 1

    @classmethod
    def get_city(cls, loc_str: str) -> 'City':
        return cls.CITIES.get(Strings.substr_to(loc_str, '.', loc_str).lower())

    @classmethod
    def get_location(cls, loc_str: str) -> 'Location':
        city_name, loc_name = loc_str.split('.')
        city = cls.get_city(city_name)
        city.LOCATIONS
        pass
