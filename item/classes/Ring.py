from gdo.shadowdogs.item.Item import Item


class Ring(Item):
    def get_slot(self) -> str:
        return 'p_ring'
    def get_default_loot_chance(self, default: int = 100) -> int:
        return 37 - self.get_level()
