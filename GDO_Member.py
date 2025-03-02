from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Party import GDT_Party
from gdo.shadowdogs.GDT_Player import GDT_Player


class GDO_Member(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Party('m_party').primary(),
            GDT_Player('m_player').primary(),
            GDT_Created('m_joined'),
        ]
