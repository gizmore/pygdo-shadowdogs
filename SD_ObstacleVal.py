from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Edited import GDT_Edited
from gdo.shadowdogs.GDT_Location import GDT_Location
from gdo.shadowdogs.GDT_Player import GDT_Player


class SD_ObstacleVal(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Player('ov_player').cascade_delete().not_null().primary(),
            GDT_Location('ov_location').not_null().primary(),
            GDT_Name('ov_obstacle').not_null().primary(),
            GDT_Name('ov_key').not_null().primary(),
            GDT_String('ov_val'),
            GDT_Edited('ov_edited'),
        ]
