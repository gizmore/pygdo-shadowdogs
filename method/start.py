from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.shadowdogs.GDT_Race import GDT_Race
from gdo.user.GDT_Gender import GDT_Gender


class start(MethodForm):

    def gdo_trigger(self) -> str:
        return 'sdstart'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Race('race').not_null(),
            GDT_Gender('gender').simple().not_null(),
        )
        super().gdo_create_form(form)

    def form_submitted(self):
        pass
