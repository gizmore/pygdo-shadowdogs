from gdo.shadowdogs.item.classes.Equipment import Equipment
from gdo.shadowdogs.item.data.items import items


class Amulet(Equipment):
    def get_slot(self) -> str:
        return 'p_amulet'

    def get_default_loot_chance(self, default: int = 100) -> int:
        return max(2, 32 - self.get_level())
