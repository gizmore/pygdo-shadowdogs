from gdo.core.GDT_UInt import GDT_UInt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Modifier(GDT_UInt):

    def __init__(self, name: str):
        super().__init__(name)
        self.bytes(2)
        self.not_null()
        self.initial('0')

    def apply(self, target: 'SD_Player'):
        target.apply(self.get_name(), self.get_value())
        return self
