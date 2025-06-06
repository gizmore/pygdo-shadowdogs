from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException


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

    def get_by_abbrev(self, val: str):
        val = val.lower()
        candidates = []
        for item in self:
            if val in item.render_name().lower():
                candidates.append(item)
        if len(candidates) == 0:
            raise ShadowdogsException('err_item_name_unknown')
        if len(candidates) > 1:
            raise ShadowdogsException('err_item_name_ambiguous')
        return candidates[0]

