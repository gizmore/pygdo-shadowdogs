from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Store import Store


class Drugstore(Store):

    ITEMS: list[tuple[Item,int]] = [
        ('Sulfur', 16),
        ('Painkiller', 6),
    ]
