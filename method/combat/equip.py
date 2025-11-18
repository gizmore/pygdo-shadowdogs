from functools import partial

from gdo.base.Application import Application
from gdo.base.Render import Render
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class equip(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdequip'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdeq'

    def sd_combat_seconds(self) -> int:
        try:
            return self.get_item().get_equip_time()
        except AttributeError:
            return 0

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').gdo(self.get_player()).inventory().not_null(),
        )
        super().gdo_create_form(form)

    def get_item(self) -> Item:
        return self.param_value('item')

    async def sd_before_execute(self):
        player = self.get_player()
        item = self.get_item()
        time = 0
        key = 'msg_sd_item_equip'
        args = []
        if old_item := player.get_equipment(item.get_slot()):
            key = 'msg_sd_item_re_equip'
            time = old_item.get_unequip_time()
            Application.EVENTS.add_timer_async(time, partial(self.unequip, player, old_item.get_slot()))
            args.append(old_item.render_name_wc())
        time += item.get_equip_time()
        player.busy(time)
        args.append(Render.bold(item.render_name_wc(), Application.get_mode()))
        args.append(item.render_slot())
        args.append(player.render_busy())
        await self.send_to_party(player.get_party(), key, tuple(args))
        if ep := player.get_enemy_party():
            await self.send_to_party(ep, key, tuple(args))
        Application.EVENTS.add_timer_async(time, partial(self.equip, player, item))
        return self.empty()

    async def sd_execute(self):
        return self.empty()

    async def equip(self, player: SD_Player, item: SD_Item) -> bool:
        item = player.inventory.remove_item(item.render_name_wc())
        item.equip()
        return True

    async def unequip(self, player: SD_Player, item_slot: str) -> bool:
        if item := player.get_equipment(item_slot):
            player.inventory.add_item(item)
            item.unequip()
            return True
        return False
