from gdo.message.GDT_HTML import GDT_HTML
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
            worked = int(q.qv_get('worked') or 0) + 1
            q.qv_set('worked', str(worked))
            if worked < Plants.WORK_TIMES:
                await self.get_party().do('work', None, Plants.WORK_TIME)
            else:
                await q.accomplished()
                await self.send_to_player(self.get_player(), 'sdqs_plants_work_done')
        return GDT_HTML()

    async def on_work_done(self):
        await self.send_to_player(self.get_player(), 'sdqs_plants_work')
        await self.give_new_items(self.get_player(), (str(Plants.WORK_REWARD)) + 'xNuyen', 'working', self.render_name())
        await self.send_to_player(self.get_player(), 'sdqs_plants_work_done')
