from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Hunger(Modifier):
    def apply(self, target: 'SD_Player'):
        target.increment(self.get_name(), self.get_value()).save()
