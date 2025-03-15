from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

from gdo.shadowdogs.attr.Attribute import Attribute


class Charisma(Attribute):
    def apply(self, target: 'GDO_Player'):
        pass
