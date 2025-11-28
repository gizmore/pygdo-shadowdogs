from gdo.base.Util import Random, gdo_print
from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.classes.Equipment import Equipment

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Weapon(Equipment):

    def get_slot(self) -> str:
        return 'p_weapon'

    def sd_commands(self) -> list[str]:
        return [
            'sdattack',
            'sdthrow',
        ]

    async def attack(self, d: 'SD_Player', armor_field: str = 'p_marm'):
        a = self.get_player()
        await self.attack_b(d, a.g('p_attack'), d.g('p_defense'), d.g('p_marm'))

    async def attack_b(self, d: 'SD_Player', attack: int, defense: int, armor: int):
        a = self.get_player()
        gdo_print(str(a.modified))
        gdo_print(str(d.modified))
        op = a.get_party()
        ep = d.get_party()
        if Random.mrand(1, attack + 1) >= Random.mrand(1, defense + 1):
            crit = ''
            dmg = Random.mrand(a.g('p_min_dmg'), a.g('p_max_dmg'))
            if Random.mrand(0, 1000) < Shadowdogs.CRIT_CHANCE_PERCENT + a.g('p_aim') * Shadowdogs.CRIT_CHANCE_PER_AIM:
                dmg += Random.mrand(0, a.g('p_min_dmg'))
                crit = '_critically'
            dmg -= armor
            if dmg <= 0:
                await self.send_to_party(op, 'sd_weapon_miss', (a.render_name(), d.render_name(), self.render_name(), a.render_busy()))
                await self.send_to_party(ep, 'sd_weapon_miss', (a.render_name(), d.render_name(), self.render_name(), a.render_busy()))
            else:
                d.deal_damage(a, dmg)
                if d.is_dead():
                    a.combat_stack().last_target = None
                    await self.send_to_party(op, 'sd_weapon_kill'+crit, (a.render_name(), d.render_name(), self.render_name(), dmg, a.render_busy()))
                    await self.send_to_party(ep, 'sd_weapon_kill'+crit, (a.render_name(), d.render_name(), self.render_name(), dmg, a.render_busy()))
                    await d.kill(a)
                else:
                    await self.send_to_party(op, 'sd_weapon_hit'+crit, (a.render_name(), d.render_name(), self.render_name(), dmg, a.render_busy()))
                    await self.send_to_party(ep, 'sd_weapon_hit_ep'+crit, (a.render_name(), d.render_name(), self.render_name(), dmg, d.gb('p_hp'), a.render_busy()))

        else:
            await self.send_to_party(op, 'sd_combat_miss', (a.render_name(), d.render_name(), self.render_name(), a.render_busy()))
            await self.send_to_party(ep, 'sd_combat_miss', (a.render_name(), d.render_name(), self.render_name(), a.render_busy()))
        return
