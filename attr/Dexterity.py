from gdo.shadowdogs.attr.Attribute import Attribute

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.Player import Player

class Dexterity(Attribute):

    def apply(self, target: 'Player'):
        pass
