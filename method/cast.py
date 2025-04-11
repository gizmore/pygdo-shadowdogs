from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Spell import GDT_Spell
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.engine.MethodSD import MethodSD


class cast(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Spell('spell').not_null(),
            GDT_TargetArg('target').friends().foes().positional(),
        )
        super().gdo_create_form(form)

    def form_submitted(self):
        pass
