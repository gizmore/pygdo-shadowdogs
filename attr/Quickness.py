from gdo.shadowdogs.attr.Attribute import Attribute

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

class Quickness(Attribute):
    def apply(self, target: 'SD_Player'):
        target.apply(self.get_name(), 1)
