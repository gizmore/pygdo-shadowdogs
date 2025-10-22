from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.item.Item import Item


class Equipment(Item):

    def get_default_loot_chance(self, default: int=100) -> int:
        return 42 - self.get_level()

    def is_equipment(self) -> bool:
        return True
