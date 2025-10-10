from functools import partial

from gdo.base.Application import Application
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class unequip(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdunequip'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sduq'

    def sd_combat_seconds(self) -> int:
        return self.get_item().get_unequip_time()

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').equipment().not_null(),
        )
        super().gdo_create_form(form)

    def get_item(self) -> Item:
        return self.param_value('item')

    async def sd_before_execute(self):
        player = self.get_player()
        item = self.get_item()
        time = item.get_unequip_time()
        player.busy(time)
        await self.send_to_player(player, 'msg_sd_item_unequip', (self.t(item.get_slot()), item.render_name_wc(), player.render_busy()))
        Application.EVENTS.add_timer_async(time, partial(self.unequip, player, item.get_slot()))
        return self.empty()

    async def sd_execute(self):
        return self.empty()

    async def unequip(self, player: SD_Player, item_slot: str) -> bool:
        if item := player.get_equipment(item_slot):
            player.inventory.add_item(item)
            item.unequip()
            return True
        return False

