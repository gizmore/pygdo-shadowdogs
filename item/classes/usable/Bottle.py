from gdo.shadowdogs.item.classes.Usable import Usable
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.Sink import Sink


class Bottle(Usable):
    def sd_can_target(self) -> bool:
        return True

    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        if isinstance(target, Sink):
            p = self.get_owner()
            p.inventory.use_item('Bottle')
            wb = await self.give_new_items(p, 'WaterBottle')
            await self.send_to_player(self.get_player(), 'msg_sd_filled_bottle', (target.render_name(), wb[0].render_name_wc()))
        else:
            await self.send_to_player(self.get_player(), 'err_sd_use_nothing_happened', (self.render_name_wc(), target.render_name()))
