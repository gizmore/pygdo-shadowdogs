from gdo.base.Util import Random
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.AreaDamage import AreaDamage
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.spells.Spell import Spell


class dart(Spell):

    def sd_cast_time(self, player: SD_Player) -> int:
        return 60 - player.g('p_int')

    def sd_mp_cost(self, player: SD_Player) -> int:
        return self.get_level() + 1

    def get_damage(self, player: SD_Player, target: SD_Player | Item) -> int:
        return Random.mrand(1, self.get_level() + 1 + (player.g('p_int') - target.g('p_int') // 4))

    def precast(self, player: SD_Player, target: SD_Player|Item):
        pass

    async def sd_cast(self, player: SD_Player, target: SD_Player | Item):
        dmg = self.get_damage(player, target)
        await AreaDamage(player, self.get_cast_text_p(player, target), self.get_cast_text_e(player, target)).deal_damage(target, dmg)
