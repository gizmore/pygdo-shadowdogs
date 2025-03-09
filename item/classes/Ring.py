from gdo.shadowdogs.item.Item import Item


class Ring(Item):
    def get_slot(self) -> str:
        return 'p_ring'
