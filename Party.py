from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created


class Party(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('party_id'),
            GDT_User('party_name'),
            GDT_Created('party_created'),
        ]

