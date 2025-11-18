from functools import partial

from gdo.base.Application import Application
from gdo.base.GDT import GDT
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.item.classes.Firearms import Firearms


class reload(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdreload'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdr'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').inventory().positional(),
        )
        super().gdo_create_form(form)

    def get_item(self) -> Item:
        if item := self.param_value('item'):
            return item
        return self.get_player().get_weapon()

    def sd_combat_seconds(self) -> int:
        time = self.get_item().dmi('rt') - self.get_player().g('p_qui') * Shadowdogs.RELOAD_SECONDS_PER_QUICKNESS
        return max(Shadowdogs.RELOAD_MIN_TIME, time)

    async def sd_before_execute(self):
        player = self.get_player()
        item = self.get_item()
        if not isinstance(item, Firearms):
            return self.err('err_sd_reload_weapon', (item.render_name(),))
        time = self.sd_combat_seconds()
        mag_size = item.dmi('mag_size')
        have_ammo = item.gdo_value('item_ammo')
        need_ammo = mag_size - have_ammo
        if not (bullets := self.get_player().inventory.get_by_name('Ammo'+item.dm('ammo'))):
            return self.err('err_sd_reload_ammo', (item.render_name(),))
        reloading = min(bullets.gdo_value('item_count'), need_ammo)
        Application.EVENTS.add_timer_async(time, partial(self.reload, player, item))
        player.busy(time)
        return self.msg('msg_sd_reloaded', (reloading, item.render_name_wc(), reloading+have_ammo))

    async def sd_execute(self):
        return self.empty()

    async def reload(self, player: SD_Player, item: Firearms) -> GDT:
        mag_size = item.dmi('mag_size')
        have_ammo = item.gdo_value('item_ammo')
        need_ammo = mag_size - have_ammo
        item_name = 'Ammo'+item.dm('ammo')
        bullets = player.inventory.get_by_name(item_name)
        reloading = min(bullets.gdo_value('item_count'), need_ammo)
        player.inventory.use_item(item_name, reloading)
        item.increment('item_ammo', reloading)
        return self.empty()
