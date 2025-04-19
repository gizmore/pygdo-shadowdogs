from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

from gdo.shadowdogs.attr.Attribute import Attribute


class Charisma(Attribute):
    def apply(self, target: 'SD_Player'):
        pass
