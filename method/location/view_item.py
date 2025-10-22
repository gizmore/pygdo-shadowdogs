from gdo.base.GDT import GDT
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class view_item(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdviewitem'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdvi'

    def sd_is_location_specific(self) -> bool:
        return True

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').store().not_null().positional(),
        )
        super().gdo_create_form(form)

    def get_target_item(self) -> Item:
        return self.param_value('item')

    async def sd_execute(self) -> GDT:
        item = self.get_target_item()
        return self.reply('msg_sd_view_item', (item.get_shop_position(), item.render_examine(),))
