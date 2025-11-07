from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.item.classes.Consumable import Consumable
from gdo.shadowdogs.item.classes.usable.Bottle import Bottle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle



class FilledBottle(Consumable, Bottle):

    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        await super().on_use(target)
        Factory.create_item('Bottle', 1, None, self.get_owner().get_id())
