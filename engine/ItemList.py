from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.engine.ShadowdogsException import SDTooMuchMatchesException, SDUnknownItemException


class ItemList(list[SD_Item]):

    def has_item(self, item_name: str) -> bool:
        return self.item_count(item_name) > 0

    def item_count(self, item_name: str) -> int:
        return self.get_by_name(item_name).get_count()

    def get_by_name(self, item_name: str) -> SD_Item | None:
        item_name = item_name.lower()
        for item in self:
            if item.render_name_wc().lower() == item_name:
                return item
        return None

    def get_by_abbrev(self, val: str) -> list[SD_Item]:
        val = val.lower()
        candidates = []
        for item in self:
            if item.render_name_wc().lower().startswith(val):
                candidates.append(item)
        if len(candidates) == 1:
            return [candidates[0]]
        candidates = []
        for item in self:
            if val in item.render_name_wc().lower():
                candidates.append(item)
        return candidates

    def get_item_by_arg(self, arg: str) -> SD_Item:
        if arg.isdigit():
            if int(arg) < 1 or int(arg) > len(self):
                raise SDUnknownItemException()
            return self[int(arg)-1]
        items = self.get_by_abbrev(arg)
        if len(items) == 1:
            return items[0]
        if len(items) > 1:
            raise SDTooMuchMatchesException(items)
        raise SDUnknownItemException()

