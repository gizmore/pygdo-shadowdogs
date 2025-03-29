from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.locations.Location import Location

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player


class GDO_KnownPlaces(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Player('kp_player').primary().cascade_delete(),
            GDT_String('kp_location').primary(),
            GDT_Created('kp_created'),
        ]

    @classmethod
    def has_location(cls, player: 'GDO_Player', location: Location):
        return cls.table().get_by_id(player.get_id(), location.get_location_key())

    @classmethod
    def give_kp(cls, player: 'GDO_Player', location: Location):
        cls.blank({
            'kp_player': player.get_id(),
            'kp_location': location.get_location_key(),
        }).insert()
