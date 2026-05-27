from gdo.shadowdogs.locations.Store import Store


class Smithers(Store):
    ITEMS: list[tuple[str, int]] = [
        ('ShortSword', 2550),
        ('Sword', 3650),
        ('LongSword', 4950),
        ('SmallAxe', 6450),
        ('MorningStar', 8150),
        ('Machete', 10050),
        ('Katana', 12150),
    ]
