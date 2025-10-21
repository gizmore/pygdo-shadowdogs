from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Edited import GDT_Edited
from gdo.shadowdogs.GDT_Player import GDT_Player

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_Quest import SD_Quest


class SD_QuestVal(GDO):

    def gdo_columns(self) -> list[GDT]:
        from gdo.shadowdogs.GDT_Quest import GDT_Quest
        return [
            GDT_Quest('qv_quest').primary().cascade_delete(),
            GDT_Player('qv_player').primary().cascade_delete(),
            GDT_Name('qv_key').primary(),
            GDT_String('qv_val').not_null(),
            GDT_Edited('qv_edited'),
            GDT_Created('qv_created'),
        ]

    @classmethod
    def qv_set(cls, quest: 'SD_Quest', player: 'SD_Player', key: str, val: str):
        if not val:
            cls.table().delete_where(f"qv_quest={quest.get_id()} AND qv_player={player.get_id()} AND qv_key='{key}'")
        else:
            cls.blank({
                'qv_quest': quest.get_id(),
                'qv_player': player.get_id(),
                'qv_key': key,
                'qv_val': val,
            }).soft_replace()

    @classmethod
    def qv_get(cls, quest: 'SD_Quest', player: 'SD_Player', key: str, default: str = None) -> str:
        val = cls.table().select('qv_val').where(f"qv_quest={quest.get_id()} AND qv_player={player.get_id()} AND qv_key='{key}'").first().exec().fetch_val()
        return val if val else default
