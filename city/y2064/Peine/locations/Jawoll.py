from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Store import Store


class Jawoll(Store):

    BEER_PRICE = 3

    ITEMS: list[tuple[Item,int]] = [
        ('Jacket', 49),
        ('Hoodie', 29),
        ('Jeans', 49),
        ('Pizza', 19),
        ('Coke', 4),
        ('LargeBeer', BEER_PRICE),
        ('Lighter', 2),
        ('Pen', 2),
        ('Petrol', 3),
    ]
