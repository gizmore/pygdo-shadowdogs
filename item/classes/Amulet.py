from gdo.shadowdogs.item.Item import Item


class Amulet(Item):
    def get_slot(self) -> str:
        return 'p_amulet'
