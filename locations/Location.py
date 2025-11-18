from functools import lru_cache
import functools

from gdo.base.GDO import GDO
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.obstacle.Obstacle import Obstacle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Location import SD_Location
    from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
    from gdo.shadowdogs.locations.City import City
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_NPC import SD_NPC



class Location(WithShadowFunc):

    GIVING: str = GDO.EMPTY_STR

    NPCS: 'list[type[TalkingNPC]]' = GDO.EMPTY_LIST
    NPC_INSTANCES: 'list[TalkingNPC]'

    OBSTACLES_INSIDE: list[Obstacle] = GDO.EMPTY_LIST
    OBSTACLES_OUTSIDE: list[Obstacle] = GDO.EMPTY_LIST

    def __init__(self):
        super().__init__()
        self.NPC_INSTANCES = []

    def __repr__(self):
        return self.get_name()

    def explore_find_chance(self, party: 'SD_Party') -> int:
        return 100

    @classmethod
    def giving_item_names(cls, player: 'SD_Player') -> str:
        return cls.GIVING

    @classmethod
    def npcs(cls, player: 'SD_Player') -> 'list[type[SD_NPC]]':
        return cls.NPCS

    def get_npcs(self, player: 'SD_Player'):
        return self.NPC_INSTANCES

    def obstacles(self, action: str, player: 'SD_Player') -> list[Obstacle]:
        obstacles = self.__class__.get_obstacles(action, player)
        for obstacle in obstacles:
            obstacle.location = self
        return obstacles

    @classmethod
    def get_obstacles(cls, action: str, player: 'SD_Player') -> list[Obstacle]:
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
        return [
        ]

    def sd_entrance_seconds(self) -> int:
        return 10

    def sd_is_respawn(self, player: 'SD_Player') -> bool:
        return False

    async def sd_on_entered(self):
        return

    async def sd_on_exited(self):
        return

    async def on_entered(self):
        await self.get_party().do(Action.INSIDE)
        await self.send_to_party(self.get_party(), 'msg_sd_entered', (self.get_location().render_name(),))

    async def on_exited(self):
        await self.get_party().do(Action.OUTSIDE)
        await self.send_to_party(self.get_party(), 'msg_sd_exited', (self.get_location().render_name(),))

    ############
    # Location #
    ############

    def get_location_id(self) -> str:
        return self.get_location_klass().get_id()

    @functools.lru_cache(maxsize=1)
    def get_location_klass(self) -> 'SD_Location':
        from gdo.shadowdogs.SD_Location import SD_Location
        return SD_Location.get_by_name(self.get_location_key())

    def get_name(self) -> str:
        return self.__class__.__name__

    @functools.cache
    def get_location_key(self) -> str:
        m = self.__class__.__module__.split('.')
        return m[3] + "." + m[4] + "." + m[-1]

    def get_city(self) -> 'City':
        return self.world().get_city(self.get_location_key())

    def lv_get(self, key: str) -> str:
        return self.get_location_klass().lv_get(key)

    def lv_set(self, key: str, val: str) -> str:
        return self.get_location_klass().lv_set(key, val)

    ###########
    # Methods #
    ###########

    async def on_search(self, player: 'SD_Player'):
        if not self.lv_get('searched') and (items := self.giving_item_names(player)):
            self.lv_set('searched', '1')
            await self.give_new_items(player, items, 'search', self.get_name())
        else:
            await self.send_to_player(player, 'msg_sd_search_nothing', (self.render_name(),))

    #########
    # Descr #
    #########

    @functools.lru_cache(maxsize=1)
    def get_t_key(self) -> str:
        return self.get_location_key().lower().replace('.', '_')

    def render_descr(self, player: 'SD_Player') -> str:
        return self.t(self.get_t_key() + '_' + player.get_action_name())

    ##########
    # Render #
    ##########

    @lru_cache
    def render_name(self) -> str:
        return self.t(self.get_t_key())
