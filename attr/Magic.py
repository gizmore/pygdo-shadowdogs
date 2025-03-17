from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

class Magic(Attribute):
    def apply(self, target: 'GDO_Player'):
        target.modified['p_max_mp'] += self.get_value() * Shadowdogs.MP_PER_MAGIC
