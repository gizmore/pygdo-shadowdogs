from gdo.shadowdogs.item.classes.Melee import Melee

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Thrust(Melee):

    async def attack(self, d: 'SD_Player', armor_field: str = 'p_marm'):
        return await super().attack(d, armor_field)
