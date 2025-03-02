from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.Player import Player


class Fight(Modifier):

    def apply(self, target: 'Player'):
        pass
