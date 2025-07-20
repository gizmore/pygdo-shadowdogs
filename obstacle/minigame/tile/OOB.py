from gdo.shadowdogs.obstacle.minigame.tile.Tile import Tile

class OOB(Tile):

    async def visit(self):
        self.disconnect(self.get_player())
        await self.send_to_player(self.get_player(), 'msg_sd_move_oob')
