from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.WithGDO import WithGDO
from gdo.shadowdogs.SD_Player import SD_Player


class GDT_City(GDT_Enum):

    _known: bool
    _default_current: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._known = False

    def known(self, known: bool = True):
        self._known = known
        return self

    def default_current(self, default_current: bool=True):
        self._default_current = default_current
        return self

    def gdo_choices(self) -> dict:
        GDO_User.current()
        return {

        }
