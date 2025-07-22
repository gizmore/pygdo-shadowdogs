import functools

from gdo.base.Application import Application
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.spells.Spell import Spell


class calm(Spell):

    def sd_mana_cost(self, player: SD_Player) -> int:
        return 5

    async def precast(self, player: SD_Player, target: SD_Player|Item):
        await self.send_to_party(player.get_party(), 'sd_cast_calm', (player.get_name(), l, target.get_name(), hp, delay))
        await self.send_to_party(player.get_enemy_party(), 'sd_cast_calm', (player.get_name(), l, target.get_name()))


    async def cast(self, player: SD_Player, target: SD_Player|Item|Obstacle=None):
        hp = l = self.get_level()
        delay = l * 60 - player.g('p_wis') * 5
        Application.EVENTS.add_timer(delay / hp, functools.partial(self.calm, player))

    def calm(self, player: SD_Player):
        player.give_hp(1)
