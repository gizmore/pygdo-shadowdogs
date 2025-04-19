from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class HP(Modifier):

    def apply(self, target: 'SD_Player'):
        if target.gdo_val('p_hp') <= 0:
            target.kill()
