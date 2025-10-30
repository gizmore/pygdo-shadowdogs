from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD


class throw(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        super().gdo_create_form(form)
