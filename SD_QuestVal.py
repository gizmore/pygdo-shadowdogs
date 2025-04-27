from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Edited import GDT_Edited
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.GDT_Quest import GDT_Quest


class SD_QuestVal(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Quest('qv_quest').primary(),
            GDT_Player('qv_player').primary(),
            GDT_Name('qv_key').primary(),
            GDT_String('qv_val').not_null(),
            GDT_Edited('qv_edited'),
            GDT_Created('qv_created'),
        ]
