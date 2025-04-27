from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Location import GDT_Location
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.locations.Location import Location


class goto(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Location('to').known().same_city().not_null(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> Location:
        return self.param_value('to')

    def form_submitted(self):
        t = self.get_target()
        p = self.get_party()
        p.do(Action.GOTO, t.get_location_key(), p.calc_goto_eta_s(t))
