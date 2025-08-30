from gdo.shadowdogs.item.Item import Item


class QuestItem(Item):

    def can_loot(self) -> bool:
        return False
