from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Store import Store


class Obi(Store):
    ITEMS: list[Item] = [
        ('Petrol', 3),
        ('WieldStick', 120),
    ]