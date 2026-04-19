from gdo.shadowdogs.city.y2064.Peine.locations.obi.Trolley import Trolley
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.SD_Player import SD_Player


class Trolleys(Obstacle):

    async def on_use(self, target: 'SD_Player|Obstacle'):

        q = Trolley.instance()
        if q.is_in_quest():
            q.accomplished()

