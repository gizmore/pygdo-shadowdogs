from gdo.base.GDT import GDT
from gdo.base.GDO import GDO
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Edited import GDT_Edited
from gdo.shadowdogs.GDT_Location import GDT_Location
from gdo.shadowdogs.GDT_Player import GDT_Player


class SD_LocationVal(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Player('lv_player').not_null().primary().cascade_delete(),
            GDT_Location('lv_location').not_null().primary().cascade_delete(),
            GDT_Name('lv_key').not_null().primary(),
            GDT_String('lv_val').case_s().ascii(),
            GDT_Edited('lv_edited'),
        ]
