from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Object import GDT_Object
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.Party import Party
from gdo.shadowdogs.Player import Player


class Member(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Object('m_party').table(Party.table()).primary(),
            GDT_Object('m_player').table(Player.table()).primary(),
            GDT_Created('m_joined'),
        ]
