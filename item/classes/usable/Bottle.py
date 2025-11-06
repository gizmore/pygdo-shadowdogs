from gdo.shadowdogs.item.classes.Usable import Usable
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Bottle(Usable):

    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        if target is None:
            return self.send_to_player(self.get_owner(), 'err_sd_use_target')
