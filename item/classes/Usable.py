from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Usable(Item):

    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        target = target or self.get_player()
        if ef := self.dm('ef'):
            for k, v in ef.items():
                target.apply(k, v)
        await self.send_use_message(target)

    async def send_use_message(self, target: 'SD_Player|Obstacle|None'):
        out = []
        for k, v in self.dm('ef').items():
            sign = '+' if v > 0 else '-'
            out.append(f"{self.t(k)}{sign}{v}")
        await self.send_to_party(self.get_party(), 'sd_use_item', (self.get_player().render_name(), self.render_name_wc(), target.render_name(), ", ".join(out), self.get_player().render_busy()))
        if ep := self.get_enemy_party():
            await self.send_to_party(ep, 'sd_use_item', (self.get_player().render_name(), self.render_name_wc(), target.render_name(), ", ".join(out), self.get_player().render_busy()))
