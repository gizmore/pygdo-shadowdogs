from gdo.shadowdogs.itembase.Melee import Melee

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player


class Fists(Melee):
    def get_actions(self, player: 'GDO_Player') -> list[str]:
        return []
    