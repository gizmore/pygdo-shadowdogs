from gdo.shadowdogs.attr.Attribute import Attribute

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

class Intelligence(Attribute):

    def apply(self, target: 'SD_Player'):
        target.apply('p_max_mp', self.get_value() * Shadowdogs.MP_PER_INTELLIGENCE)
