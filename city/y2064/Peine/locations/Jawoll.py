from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Store import Store


class Jawoll(Store):

    ITEMS: list[tuple[Item,int]] = [
        ('Pizza', 25),
        ('Coke', 15),
        ('Lighter', 3),
        ('Jacket', 49),
        ('Hoodie', 35),
    ]
