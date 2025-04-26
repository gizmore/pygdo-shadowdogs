from gdo.shadowdogs.SD_Item import SD_Item

class Inventory(list[SD_Item]):

    def __init__(self):
        super().__init__()
        pass

    def has_item(self, item_name: str) -> bool:
        return self.item_count(item_name) > 0

    def item_count(self, item_name: str) -> int:
        count = 0
        for item in self:
            if item.get_name() == item_name:
                count += item.get_count()
        return count
