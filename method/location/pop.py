from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class pop(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdpop'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdpo'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_ItemArg('item').bank().not_null(),
        )
        super().gdo_create_form(form)

    def get_item(self) -> Item:
        return self.param_value('item')

    async def sd_execute(self):
        return self.get_location().on_pop(self.get_player(), self.get_item())
