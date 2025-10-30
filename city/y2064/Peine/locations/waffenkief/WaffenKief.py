from gdo.shadowdogs.city.y2064.Peine.locations.waffenkief.Cashier import Cashier
from gdo.shadowdogs.locations.Store import Store
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class WaffenKief(Store):

    NPCS: 'list[type[TalkingNPC]]' = [
        Cashier,
    ]

    ITEMS: list[tuple[str,int]] = [
        ('BronzeKnuckles', 100),
        ('SteelKnuckles', 250),
        ('ShortSword', 800),
        ('Pistol', 2200),
        ('Shotgun', 22500),
        ('Ammo9mm', 80),
        ('Ammo12g', 150),
        ('KevlarVest', 37500),
    ]
