from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.engine.MethodSD import MethodSD


class use(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').inventory().equipment().not_null(),
            GDT_TargetArg('target').me().obstacles().friends().foes().positional(),
        )
        super().gdo_create_form(form)

    def get_item(self) -> SD_Item:
        return self.param_value('item')

    def sd_combat_seconds(self) -> float:
        return self.get_item().itm().sd_attack_time()

    def form_submitted(self):
        pass

