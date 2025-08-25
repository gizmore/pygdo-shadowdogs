from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.GDT_Spell import GDT_Spell
from gdo.shadowdogs.engine.MethodSD import MethodSD


class gmsp(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Player('to').humans().not_null(),
            GDT_Spell('spell').not_null(),
        )
        super().gdo_create_form(form)

    def sd_execute(self):
        pass
    