from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.GDT_Target import GDT_Target
from gdo.shadowdogs.engine.MethodSD import MethodSD


class use(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').obstacles().inventory().equipment().not_null(),
            GDT_Target('target').positional()
        )
        super().gdo_create_form(form)

    def form_submitted(self):
        pass
