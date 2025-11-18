from gdo.shadowdogs.item.classes.Weapon import Weapon

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Firearms(Weapon):

    def is_stackable(self) -> bool:
        return False

    async def attack(self, d: 'SD_Player', armor_field: str = 'p_farm'):
        a = self.get_player()
        return await self.attack_b(d, a.g('p_attack'), d.g('p_defense'), d.g('p_farm'))
