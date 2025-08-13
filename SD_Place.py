from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Location import GDT_Location
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Location import SD_Location

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.locations.Location import Location


class SD_Place(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Player('kp_player').npcs().primary().cascade_delete(),
            GDT_Location('kp_location').primary(),
            GDT_Created('kp_created'),
        ]

    def get_player(self) -> 'SD_Player':
        return self.gdo_value('kp_player')

    @classmethod
    def has_location(cls, player: 'SD_Player', location: 'Location'):
        loc = SD_Location.get_or_create(location)
        return cls.table().get_by_id(player.get_id(), loc.get_id())

    @classmethod
    def give_kp(cls, player: 'SD_Player', location: 'Location'):
        loc = SD_Location.get_or_create(location)
        return cls.blank({
            'kp_player': player.get_id(),
            'kp_location': loc.get_id(),
        }).insert()

    def get_location(self) -> 'Location':
        from gdo.shadowdogs.engine.World import World
        return World.get_location(self.gdo_val('kp_location'))
