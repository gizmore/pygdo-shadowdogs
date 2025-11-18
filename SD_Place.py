from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Query import Query
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Location import GDT_Location
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Location import SD_Location

from typing import TYPE_CHECKING

from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.locations.Location import Location


class SD_Place(WithShadowFunc, GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Player('kp_player').npcs().primary().cascade_delete(),
            GDT_Location('kp_location').primary(),
            GDT_Created('kp_found'),
        ]

    @classmethod
    def query_for_player(cls, player: 'SD_Player') -> Query:
        return cls.table().select().where(f'kp_player={player.get_id()}')

    @classmethod
    def has_location(cls, player: 'SD_Player', location: 'Location'):
        loc = SD_Location.get_or_create(location)
        return cls.table().get_by_id(player.get_id(), loc.get_id())

    @classmethod
    def give_place(cls, player: 'SD_Player', location: 'Location'):
        loc = SD_Location.get_or_create(location)
        return cls.blank({
            'kp_player': player.get_id(),
            'kp_location': loc.get_id(),
        }).insert()

    #
    def get_player(self) -> 'SD_Player':
        return self.gdo_value('kp_player')

    def get_sd_location(self) -> SD_Location:
        return self.gdo_value('kp_location')

    def get_location(self) -> 'Location':
        return self.world().get_location(self.get_sd_location().gdo_val('l_name'))

    def render_name(self):
        return self.get_location().render_name()
