from gdo.shadowdogs.item.Item import Item


class Boots(Item):
    def get_slot(self) -> str:
        return 'p_boots'
