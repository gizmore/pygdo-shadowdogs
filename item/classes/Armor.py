from gdo.shadowdogs.item.Item import Item


class Armor(Item):

    def get_slot(self) -> str:
        return 'p_armor'
