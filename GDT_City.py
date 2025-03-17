from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.WithGDO import WithGDO
from gdo.shadowdogs.GDO_Player import GDO_Player


class GDT_City(GDT_Enum):

    _known: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._known = False

    def known(self, known: bool = True):
        self._known = known
        return self

    def gdo_choices(self) -> dict:
        GDO_User.current()
        return {

        }
