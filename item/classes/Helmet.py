from gdo.shadowdogs.item.Item import Item


class Helmet(Item):
    def get_slot(self) -> str:
        return 'p_helmet'

