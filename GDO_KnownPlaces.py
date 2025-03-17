from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_String import GDT_String
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Player import GDT_Player


class GDO_KnownPlaces(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Player('kp_user').primary().cascade_delete(),
            GDT_String('kp_location').primary(),
            GDT_Created('kp_created'),
        ]
