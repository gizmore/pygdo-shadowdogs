from gdo.shadowdogs.item.Item import Item


class Rune(Item):
    def get_default_loot_chance(self, default: int = 100) -> int:
        return 37 - self.get_level()
