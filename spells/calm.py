import functools

from gdo.base.Application import Application
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.spells.Spell import Spell


class calm(Spell):

    def sd_mp_cost(self, player: SD_Player) -> int:
        return 3 + self.get_level()

    def sd_cast_time(self, player: SD_Player) -> int:
        return 60 - player.g('p_int') - self.get_level()

    def get_hp_gain(self):
        return self.get_level() + (self.get_player().g('p_int') // 4) - 1

    def get_hp_delay(self):
        return max(20, 60 - self.get_player().g('p_wis'))

    async def sd_cast(self, player: SD_Player, target: SD_Player | Item | Obstacle=None):
        l = self.get_level()
        hp = self.get_hp_gain()
        delay = self.get_hp_delay()
        Application.EVENTS.add_timer(delay / hp, functools.partial(self.calm, player), hp)
        await self.send_to_party(player.get_party(), 'sd_cast_calm', (player.get_name(), l, target.get_name(), hp, delay))
        if ep := player.get_enemy_party():
            await self.send_to_party(ep, 'sd_cast_calm', (player.get_name(), l, target.get_name()))

    async def calm(self, player: SD_Player):
        player.give_hp(1)
