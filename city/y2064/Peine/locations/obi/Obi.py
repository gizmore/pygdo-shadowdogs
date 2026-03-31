from gdo.shadowdogs.city.y2064.Peine.locations.obi.Felix import Felix
from gdo.shadowdogs.city.y2064.Peine.locations.obi.GardenWitch import GardenWitch
from gdo.shadowdogs.city.y2064.Peine.locations.obi.Plants import Plants
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Store import Store
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Obi(Store):

    NPCS: 'list[type[TalkingNPC]]' = [
        Felix,
        GardenWitch,
    ]

    ITEMS: list[Item] = [
        ('Petrol', 3),
        ('WieldStick', 120),
    ]

    def sd_methods(self) -> list[str]:
        return [
            'sdwork',
        ] + super().sd_methods()

    async def on_work(self):
        q = Plants.instance()
        if q.is_in_quest():
            pass