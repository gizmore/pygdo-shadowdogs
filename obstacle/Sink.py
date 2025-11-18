from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Sink(Obstacle):

    async def on_use(self, target: 'SD_Player|Obstacle'):
        await self.send_to_player(self.get_player(), 'msg_sd_drink_pond')
        self.get_player().increment('p_thirst', 10)
