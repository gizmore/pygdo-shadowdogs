from gdo.core.GDT_UInt import GDT_UInt
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class drop(MethodSD):
    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_ItemArg('item').inventory().not_null(),
        )
        super().gdo_create_form(form)

    def get_item(self) -> Item:
        return self.param_value('item')

    async def sd_execute(self):
        item = self.get_item()
        self.get_player().inventory.remove_item(item.render_name())
        item.delete()
        return self.msg('msg_sd_dropped_item', (item.render_name(),))
