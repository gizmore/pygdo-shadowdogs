from gdo.base.Trans import t
from gdo.message.GDT_HTML import GDT_HTML
from gdo.shadowdogs.item.classes.Usable import Usable


class Consumable(Usable):
    async def on_use(self):
        player = self.get_player()
        ef = []
        for key,value in self.dm('ef'):
            player.apply(key, value)
            sign = '+' if value > 0 else '-'
            sign = '' if value == 0 else sign
            ef.append(f"{t(f'sd_{key}')}({sign}{value})")
        if not ef:
            ef.append(t('none'))
        await self.send_to_party(player.get_party(), 'msg_sd_consumed', (self.render_name(), ",".join(ef), player.render_busy()))
        return GDT_HTML()
