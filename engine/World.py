from gdo.base.Util import Strings
from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.city.Peine.Peine import Peine
from gdo.shadowdogs.city.AmBauhof15.AmBauhof15 import AmBauhof15
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.npcs.Mob import Mob
from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.locations.Location import Location

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City
    from gdo.shadowdogs.SD_Player import SD_Player


class World:
    NPCs: dict[str, type[SD_NPC]] = {
        'mob': Mob,
    }

    Peine: Peine = Peine()
    AmBauhof15: AmBauhof15 = AmBauhof15()

    CITIES: dict[str, 'City'] = {
        'peine': Peine,
        'ambauhof15': AmBauhof15,
    }

    @classmethod
    def get_player_for_user(cls, user: GDO_User) -> 'SD_Player|None':
        return Shadowdogs.USERMAP.get(user.get_id())

    @classmethod
    def get_city(cls, loc_str: str) -> 'City | None':
        city_key = Strings.substr_to(loc_str, '.', loc_str).lower()
        return cls.CITIES.get(city_key)

    @classmethod
    def get_location(cls, loc_str: str) -> 'Location':
        city_name, loc_name = loc_str.split('.', 1)
        city = cls.get_city(city_name)
        if city is None:
            raise ValueError(f"Unknown city: {city_name}")
        location = getattr(city, loc_name, None)
        if location is None:
            raise ValueError(f"Unknown location: {loc_str}")
        return location

    @classmethod
    def get_npc_class(cls, name: str) -> type[SD_NPC]:
        return cls.NPCs.get(name.lower(), Mob)
