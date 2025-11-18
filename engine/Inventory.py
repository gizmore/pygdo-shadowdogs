import re

from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.engine.ItemList import ItemList


class Inventory(WithShadowFunc, ItemList):

    Factory = None

    def add_item(self, item: Item) -> Item:
        if item.is_stackable() and (old_item := self.get_by_name(item.render_name_wc())):
            old_item.increment('item_count', item.get_count())
            item.delete()
            return old_item
        else:
            self.append(item)
            item.save()
            return item

    def remove_item(self, item_name: str) -> Item|None:
        count = 1
        if m := re.match(r"^(\d+)x(.*)$", item_name):
            count = int(m.group(1))
            item_name = m.group(2)
        if item := self.get_by_name(item_name):
            if item.get_count() <= count:
                self.remove(item)
                return item
            item.increment('item_count', -count)
            return self.factory().create_item(item_name, count, item.get_modifier_name())
        return None

    def use_item(self, item_name: str, count: int=1):
        if item := self.get_by_name(item_name):
            item.increment('item_count', -count)
            if item.get_count() < 1:
                self.remove(item)
                item.delete()
