from gdo.shadowdogs.SD_Item import SD_Item


class Inventory(list[SD_Item]):

    Factory = None

    def __init__(self):
        super().__init__()

    def has_item(self, item_name: str) -> bool:
        return self.item_count(item_name) > 0

    def item_count(self, item_name: str) -> int:
        return self.get_by_name(item_name).get_count()

    def get_by_name(self, item_name: str) -> SD_Item|None:
        item_name = item_name.lower()
        for item in self:
            if item.render_name().lower() == item_name:
                return item
        return None

    def get_by_abbrev(self, val: str) -> list[SD_Item]:
        val = val.lower()
        candidates = []
        for item in self:
            if item.render_name().lower().startswith(val):
                candidates.append(item)
        if len(candidates) == 1:
            return [candidates[0]]
        candidates = []
        for item in self:
            if val in item.render_name().lower():
                candidates.append(item)
        return candidates

    def add_item(self, item: SD_Item) -> SD_Item:
        if old_item := self.get_by_name(item.render_name()):
            old_item.increment('item_count', item.get_count())
            item.delete()
            return old_item
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