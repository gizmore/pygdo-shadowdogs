import functools

from gdo.base.GDO import GDO
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.obstacle.Obstacle import Obstacle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City
    from gdo.shadowdogs.SD_Player import SD_Player


class Location(WithShadowFunc):

    OBSTACLES: dict[str,list[Obstacle]] = {
        Action.INSIDE: [],
        Action.OUTSIDE: [],
    }

    ############
    # Abstract #
    ############

    def sd_explore_chance(self) -> int:
        return 100

    def sd_methods(self) -> list[str]:
        return GDO.EMPTY_LIST

    ############
    # Location #
    ############

    def get_name(self) -> str:
        return self.__class__.__name__

    @functools.cache
    def get_location_key(self) -> str:
        m = self.__class__.__module__.split('.')
        return m[3] + "." + m[5]

    def get_city(self) -> 'City':
        from gdo.shadowdogs.engine.World import World
        return World.get_city(self.get_location_key())

    ###########
    # Methods #
    ###########

    async def on_search(self, player: 'SD_Player'):
        await self.send_to_player(player, 'msg_sd_search_nothing')

    ##########
    # Render #
    ##########

    def render_name(self) -> str:
        return self.t(self.get_location_key().lower())

