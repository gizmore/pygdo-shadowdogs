from gdo.shadowdogs.item.classes.Weapon import Weapon

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Firearms(Weapon):

    async def attack(self, d: 'SD_Player', armor_field: str = 'p_farm'):
        return await super().attack(d, armor_field)
