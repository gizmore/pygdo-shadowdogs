from gdo.shadowdogs.attr.Attribute import Attribute

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

class Dexterity(Attribute):

    def apply(self, target: 'GDO_Player'):
        target.apply(self.get_name(), self.get_value())
        target.apply('p_attack', self.get_value())
