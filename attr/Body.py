from gdo.shadowdogs.attr.Attribute import Attribute
from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Body(Attribute):

    def apply(self, target: 'SD_Player'):
        target.apply(self.get_name(), self.get_value())
        target.apply('p_max_hp', self.get_value() * Shadowdogs.HP_PER_BODY)
