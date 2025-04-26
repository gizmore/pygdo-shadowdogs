from gdo.base.Util import Random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item


class Weapon(Item):

    def get_slot(self) -> str:
        return 'p_weapon'

    def get_actions(self) -> list[str]:
        return ['attack']

    async def attack(self, target: 'SD_Player'):
        a = self._owner
        p = self._owner.get_party()
        ep = target.get_party()
        if Random.mrand(0, self._owner.g('p_atk')) >= Random.mrand(0, target.g('p_def')):
            dmg = Random.mrand(self.min_dmg, self.max_dmg) - target.g('p_marm')
            target.hit(dmg)
        else:
            p.send('sd_combat_miss', (a.render_name(), target.render_name(), self.render_name(), self.get_attack_time()))
