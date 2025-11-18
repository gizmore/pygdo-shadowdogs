from gdo.shadowdogs.item.classes.Melee import Melee

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Fists(Melee):

    def can_loot(self) -> bool:
        return False

    def can_sell(self) -> bool:
        return False
