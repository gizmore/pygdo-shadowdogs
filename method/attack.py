from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Target import GDT_Target
from gdo.shadowdogs.engine.MethodSD import MethodSD


class attack(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_Target('target'))
        super().gdo_create_form(form)
