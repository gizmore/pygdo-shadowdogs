from gdo.shadowdogs.city.y2064.Peine.locations.obi.Felix import Felix
from gdo.shadowdogs.city.y2064.Peine.locations.obi.GardenWitch import GardenWitch
from gdo.shadowdogs.city.y2064.Peine.locations.obi.Plants import Plants
from gdo.shadowdogs.city.y2064.Peine.locations.obi.Trolleys import Trolleys
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Store import Store
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Obi(Store):

    NPCS: 'list[type[TalkingNPC]]' = [
        Felix,
        GardenWitch,
    ]

    ITEMS: list[Item] = [
        ('Petrol', 3),
        ('WieldStick', 120),
    ]

    OBSTACLES_OUTSIDE: list[Obstacle] = [
        Trolleys(),
    ]

    def sd_methods(self) -> list[str]:
        return [
            'sdwork',
        ] + super().sd_methods()

    async def on_work(self):
        q = Plants.instance()
        if q.is_in_quest():
            worked = int(q.qv_get('worked')) + 1
            q.qv_set('worked', str(worked))
            if worked < 8:
                await self.send_to_player(self.get_player(), 'sdqs_plants_work')
                await self.give_new_items(self.get_player(), '50xNuyen', 'working', self.render_name())
            else:
                await q.accomplished()
