from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.attr.Attribute import Attribute

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

class Strength(Attribute):
    def apply(self, target: 'GDO_Player'):
        target.apply('p_max_weight', self.get_value() * Shadowdogs.MAX_WEIGHT_PER_STRENGTH)
        target.apply('p_max_hp', self.get_value() * Shadowdogs.HP_PER_STRENGTH)
