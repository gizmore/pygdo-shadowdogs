from gdo.core.GDT_String import GDT_String
from typing import TYPE_CHECKING

from gdo.shadowdogs.actions.Action import Action

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class GDT_Target(GDT_String):

    _last_target: bool

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_s()
        self.maxlen(255)
        self._last_target = False

    def get_party(self) -> 'SD_Party':
        return self._gdo

    def last_target(self, last_target: bool = True):
        self._last_target = last_target
        return self

    def get_action(self) -> 'Action':
        party = self.get_party()
        return party.get_last_action() if self._last_target else party.get_action()

    def get_target_string(self) -> str:
        party = self.get_party()
        return party.get_last_target_string() if self._last_target else party.get_target_string()

    def get_value(self):
        action = self.get_action()
        return action.get_target(self.get_party(), self.get_target_string())
