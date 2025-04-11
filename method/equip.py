from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDO_Item import GDO_Item
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class equip(MethodSD):

    def sd_combat_seconds(self) -> int:
        return self.get_item().get_equip_time()

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').inventory().not_null(),
        )
        super().gdo_create_form(form)

    def get_gdo_item(self) -> GDO_Item:
        return self.param_value('item')

    def get_item(self) -> Item:
        return self.get_gdo_item().get_item()

    def form_submitted(self):
        pass