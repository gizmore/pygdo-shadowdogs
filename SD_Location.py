from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name
from gdo.date.GDT_Created import GDT_Created


class SD_Location(GDO):

    def gdo_persistent(self) -> bool:
        return False

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('l_id'),
            GDT_Name('l_name'),
            GDT_Created('l_created'),
        ]

