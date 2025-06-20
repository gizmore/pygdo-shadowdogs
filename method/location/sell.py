from gdo.base.GDT import GDT
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.engine.MethodSD import MethodSD


class sell(MethodSD):

    def sd_is_location_specific(self) -> bool:
        return True

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_ItemArg('item').inventory().not_null())
        super().gdo_create_form(form)

    def gdo_execute(self) -> GDT:
        pass
