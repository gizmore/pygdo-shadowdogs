import functools

from gdo.base.GDO import GDO
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.obstacle.Obstacle import Obstacle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_NPC import SD_NPC


class Location(WithShadowFunc):

    GIVING: str = GDO.EMPTY_STR

    NPCS: list['SD_NPC'] = GDO.EMPTY_LIST

    OBSTACLES_INSIDE: list[Obstacle] = GDO.EMPTY_LIST
    OBSTACLES_OUTSIDE: list[Obstacle] = GDO.EMPTY_LIST

    def explore_find_chance(self, party: 'SD_Party') -> int:
        return 100

    @classmethod
    def giving_item_names(cls, player: 'SD_Player') -> str:
        return cls.GIVING

    @classmethod
    def npcs(cls, player: 'SD_Player') -> 'list[SD_NPC]':
        return cls.NPCS

    @classmethod
    def obstacles(cls, action: str, player: 'SD_Player') -> list[Obstacle]:
        if action == Action.INSIDE:
            return cls.OBSTACLES_INSIDE
        elif action == Action.OUTSIDE:
            return cls.OBSTACLES_OUTSIDE
        return GDO.EMPTY_LIST

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
        return m[3] + "." + m[-3] + "." + m[-1]

    def get_city(self) -> 'City':
        from gdo.shadowdogs.engine.World import World
        return World.get_city(self.get_location_key())

    ###########
    # Methods #
    ###########

    async def on_search(self, player: 'SD_Player'):
        if items := self.giving_item_names(player):
            await self.give_new_items(player, items, 'search', self.get_name())
        else:
            await self.send_to_player(player, 'msg_sd_search_nothing')

    ##########
    # Render #
    ##########

    def render_name(self) -> str:
        return self.t(self.get_location_key().lower().replace('.', '_'))

