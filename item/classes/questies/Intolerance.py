from gdo.shadowdogs.city.y2064.Oberg.locations.granny.Lecture import Lecture
from gdo.shadowdogs.item.Item import Item
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Intolerance(Item):

    async def on_use(self, target: 'SD_Player|Obstacle'):
        await self.send_to_player(target, 'sdqs_intolerance')
        await Lecture.instance().on_accomplished()
