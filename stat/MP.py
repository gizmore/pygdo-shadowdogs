from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

from gdo.shadowdogs.engine.Modifier import Modifier

class MP(Modifier):

    def apply(self, target: 'GDO_Player'):
        pass
