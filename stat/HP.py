from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player


class HP(Modifier):

    def apply(self, target: 'GDO_Player'):
        if target.gdo_val('p_hp') <= 0:
            target.kill()
