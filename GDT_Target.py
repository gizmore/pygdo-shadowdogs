from gdo.core.GDT_String import GDT_String
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class GDT_Target(GDT_String):

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_s()
        self.maxlen(96)

    def get_party(self) -> 'SD_Party':
        return self._gdo

    def get_value(self):
        party = self.get_party()
        return party.get_action().get_target(party)
