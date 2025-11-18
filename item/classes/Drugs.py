from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.classes.Consumable import Consumable
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Drugs(Consumable):

    async def on_use(self, target: 'SD_Player|Obstacle'):
        await super().on_use(target)
        await self.send_to_player(self.get_player(), 'msg_sd_drugs_bad')
