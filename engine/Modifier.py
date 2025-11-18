from typing import TYPE_CHECKING

from gdo.core.GDT_Int import GDT_Int

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Modifier(GDT_Int):

    def __init__(self, name: str):
        super().__init__(name)
        self.bytes(2)
        self.not_null()
        self.initial('0')

    def apply(self, target: 'SD_Player'):
        value = self.get_value()
        if value > 0:
            target.apply(self.get_name(), self.get_value())
        return self
