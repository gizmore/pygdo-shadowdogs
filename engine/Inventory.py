from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.engine.ItemList import ItemList


class Inventory(ItemList):

    Factory = None

    def add_item(self, item: SD_Item) -> SD_Item:
        if item.is_stackable() and (old_item := self.get_by_name(item.render_name_wc())):
            old_item.increment('item_count', item.get_count())
            item.delete()
            return old_item
        else:
            self.append(item)
            item.save()
            return item

    def remove_item(self, item_name: str, count: int=1) -> SD_Item|None:
        if not self.__class__.Factory:
            from gdo.shadowdogs.engine.Factory import Factory
            self.__class__.Factory = Factory
        if item := self.get_by_name(item_name):
            if item.get_count() < count:
                return None
            if count == 1:
                self.remove(item)
                return item
            item.increment('item_count', -count)
            return self.__class__.Factory.create_item(item_name, count, item.get_modifier_name())
        return None

    def use_item(self, item_name: str, count: int=1):
        if item := self.get_by_name(item_name):
            item.increment('item_count', -count)
            if item.get_count() < 1:
                self.remove(item)
                item.delete()
