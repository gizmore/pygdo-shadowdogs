from gdo.base.Trans import t
from gdo.message.GDT_HTML import GDT_HTML
from gdo.shadowdogs.item.classes.Usable import Usable

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle

class Consumable(Usable):

    def sd_use_time(self) -> int:
        return self.get_weight() // 2

    def sd_can_use_on_self(self) -> bool:
        return True

    async def on_use(self, target: 'SD_Player|Obstacle'):
        player = self.get_player()
        ef = []
        for key, value in self.dm('ef', {}).items():
            key = f"p_{key}"
            player.incb(key, value)
            sign = '+' if value > 0 else ''
            ef.append(f"{t(key)}({sign}{value})")
        if not ef:
            ef.append(t('none'))
        self.use(1)
        await self.send_to_party(player.get_party(), 'msg_sd_consumed', (self.render_name(), ",".join(ef), player.render_busy()))
        return GDT_HTML()
