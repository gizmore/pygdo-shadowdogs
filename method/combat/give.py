from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class give(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Player('to').npcs().nearby().not_null(),
            GDT_ItemArg('item').inventory().not_null(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> SD_Player:
        return self.param_value('to')

    def get_item(self) -> Item:
        return self.param_value('item')

    async def sd_execute(self):
        p = self.get_player()
        to = self.get_target()
        item = self.get_item()
        count = Item.get_count_from_item_name(self.param_val('item'))
        item = p.inventory.remove_item(item.render_name_wc(), count)
        # p.busy(self.sd_combat_seconds())
        self.msg('msg_sd_give_item', (item.render_name(), to.render_name(), ''))
        await self.give_item(to, item, 'gave', self.get_player().render_name())
        return self.empty()
