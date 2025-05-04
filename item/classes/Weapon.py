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

    async def attack(self, d: 'SD_Player', armor_field: str = 'p_marm'):
        a = self.get_player()
        op = a.get_party()
        ep = d.get_party()
        if Random.mrand(0, a.g('p_attack')) >= Random.mrand(0, d.g('p_defense')):
            dmg = Random.mrand(a.g('p_min_dmg'), a.g('p_max_dmg')) - d.g(armor_field)
            if dmg <= 0:
                await self.send_to_party(op, 'sd_weapon_miss', (a.render_name(), d.render_name(), self.render_name(), a.render_busy()))
                await self.send_to_party(ep, 'sd_weapon_miss', (a.render_name(), d.render_name(), self.render_name(), a.render_busy()))
            else:
                d.hit(dmg)
                if d.is_dead():
                    a.combat_stack.last_target = None
                    await self.send_to_party(op, 'sd_weapon_kill', (a.render_name(), d.render_name(), self.render_name(), dmg, a.render_busy()))
                    await self.send_to_party(ep, 'sd_weapon_kill', (a.render_name(), d.render_name(), self.render_name(), dmg, a.render_busy()))
                    await d.kill()
                else:
                    await self.send_to_party(op, 'sd_weapon_hit', (a.render_name(), d.render_name(), self.render_name(), dmg, a.render_busy()))
                    await self.send_to_party(ep, 'sd_weapon_hit_ep', (a.render_name(), d.render_name(), self.render_name(), dmg, a.render_busy()))

        else:
            await self.send_to_party(op, 'sd_combat_miss', (a.render_name(), d.render_name(), self.render_name(), self.sd_attack_time()))
            await self.send_to_party(ep, 'sd_combat_miss', (a.render_name(), d.render_name(), self.render_name(), self.sd_attack_time()))
