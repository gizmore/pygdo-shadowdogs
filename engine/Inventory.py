from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException


class Inventory(list[SD_Item]):

    def __init__(self):
        super().__init__()

    def has_item(self, item_name: str) -> bool:
        return self.item_count(item_name) > 0

    def item_count(self, item_name: str) -> int:
        count = 0
        for item in self:
            if item.get_name() == item_name:
                count += item.get_count()
        return count

    def get_by_abbrev(self, val: str) -> list[SD_Item]:
        val = val.lower()
        candidates = []
        for item in self:
            if val in item.render_name().lower():
                candidates.append(item)
        return candidates
