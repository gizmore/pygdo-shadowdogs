from gdo.shadowdogs.city.y2064.Peine.locations.car_repair.Peter import Peter
from gdo.shadowdogs.locations.Store import Store


class CarRepairShop(Store):
    ITEMS: list[tuple[str, int]] = [
        'WieldKit'
    ]

    NPCS: 'list[type[TalkingNPC]]' = [
        Peter,
    ]
