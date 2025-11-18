import re

from gdo.shadowdogs.engine.ShadowdogsException import SDTooMuchMatchesException, SDUnknownItemException
from gdo.shadowdogs.item.Item import Item


class ItemList(list[Item]):

    def has_item(self, item_name: str, count: int=1) -> bool:
        if m := re.match(r"^(\d+)x(.*)$", item_name):
            count = int(m.group(1))
            item_name = m.group(2)
        return self.item_count(item_name) >= count

    def item_count(self, item_name: str) -> int:
        if item := self.get_by_name(item_name):
            return item.get_count()
        return 0

    def get_by_name(self, item_name: str) -> Item | None:
        item_name = item_name.lower()
        for item in self:
            if item.render_name_wc().lower() == item_name:
                return item
        return None

    def get_by_abbrev(self, val: str) -> list[Item]:
        val = val.lower()
        candidates = []
        for item in self:
            name = item.render_name_wc().lower()
            if name.startswith(val):
                candidates.append(item)
            if name == val:
                return [item]
        if len(candidates) == 1:
            return [candidates[0]]
        candidates = []
        for item in self:
            if val in item.render_name_wc().lower():
                candidates.append(item)
        return candidates

    def get_item_by_arg(self, arg: str) -> Item:
        if arg.isdigit():
            if int(arg) < 1 or int(arg) > len(self):
                raise SDUnknownItemException(arg)
            return self[int(arg)-1]
        items = self.get_by_abbrev(arg)
        if len(items) == 1:
            return items[0]
        if len(items) > 1:
            raise SDTooMuchMatchesException(items)
        raise SDUnknownItemException(arg)

