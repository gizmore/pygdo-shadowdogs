from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.city.y2064.World2064 import World2064
from gdo.shadowdogs.city.y2077.World2077 import World2077
from gdo.shadowdogs.city.y2088.World2088 import World2088
from gdo.shadowdogs.engine.Loader import Loader
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations.Location import Location

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class World:

    World2064: World2064 = World2064()
    World2077: World2077 = World2077()
    World2088: World2088 = World2088()

    WORLDS = {
        'y2064': World2064,
        'y2077': World2077,
        'y2088': World2088,
    }

    @classmethod
    def get_player_for_user(cls, user: GDO_User) -> 'SD_Player|None':
        Loader.load_user(user)
        return Shadowdogs.USERMAP.get(user.get_id())

    @classmethod
    def get_city(cls, loc_str: str) -> 'City | None':
        year, city_name, loc_name = loc_str.split('.', 2)
        return cls.WORLDS.get(year).CITIES.get(city_name)

    @classmethod
    def get_location(cls, loc_str: str) -> 'Location':
        try:
            year, city_name, loc_name = loc_str.split('.', 2)
        except ValueError:
            return cls.get_city(loc_str+'.fake')
        city = cls.get_city(loc_str)
        if city is None:
            raise ValueError(f"Unknown city: {loc_str}")
        location = getattr(city, loc_name, None)
        if location is None:
            raise ValueError(f"Unknown location: {loc_str}")
        return location

    # @classmethod
    # def get_npc_class(cls, name: str) -> type[SD_NPC]:
    #     return npcs.NPCS.NPCS.NPCScls.NPCs.get(name.lower(), Mob)
