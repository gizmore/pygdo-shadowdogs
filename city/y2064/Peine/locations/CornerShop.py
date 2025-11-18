from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Store import Store


class CornerShop(Store):

    ITEMS: list[tuple[Item,int]] = [
        ('Apple', 3),
        ('Saltpeter', 5),
    ]
