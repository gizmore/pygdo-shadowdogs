from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.SD_Player import SD_Player


class GDT_Executable(GDT_Enum):

    _all: bool

    def __init__(self, name: str):
        super().__init__(name)

    def all(self, all: bool = True):
        self._all = all
        return self

    def get_player(self) -> SD_Player:
        return self._gdo
