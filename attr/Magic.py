from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

class Magic(Attribute):
    def apply(self, target: 'SD_Player'):
        super().apply(target)
        target.modified['p_max_mp'] += self.get_value() * Shadowdogs.MP_PER_MAGIC
