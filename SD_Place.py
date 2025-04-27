from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Location import GDT_Location
from gdo.shadowdogs.GDT_Player import GDT_Player

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.locations.Location import Location


class SD_Place(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Player('kp_player').primary().cascade_delete(),
            GDT_Location('kp_location').primary(),
            GDT_Created('kp_created'),
        ]

    @classmethod
    def has_location(cls, player: 'SD_Player', location: 'Location'):
        return cls.table().get_by_id(player.get_id(), location.get_location_key())

    @classmethod
    def give_kp(cls, player: 'SD_Player', location: 'Location'):
        cls.blank({
            'kp_player': player.get_id(),
            'kp_location': location.get_location_key(),
        }).insert()
