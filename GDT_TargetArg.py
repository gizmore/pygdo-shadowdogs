from gdo.core.GDT_String import GDT_String
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party


class GDT_TargetArg(GDT_String):

    _obstacles: bool
    _friends: bool
    _foes: bool


    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_s()
        self.maxlen(96)
        self._obstacles = False
        self._friends = False
        self._foes = False

    def obstacles(self, obstacles: bool = True):
        self._obstacles = obstacles
        return self

    def friends(self, friends: bool = True):
        self._friends = friends
        return self

    def foes(self, foes: bool = True):
        self._foes = foes
        return self
