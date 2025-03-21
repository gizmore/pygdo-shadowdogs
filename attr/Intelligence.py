from gdo.shadowdogs.attr.Attribute import Attribute

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

class Intelligence(Attribute):

    def apply(self, target: 'GDO_Player'):
        target.apply(self.get_name(), self.get_value())
        target.apply('p_max_mp', self.get_value() * Shadowdogs.MP_PER_INTELLIGENCE)
