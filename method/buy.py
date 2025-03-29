from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.MethodSD import MethodSD


class buy(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').store().not_null(),
        )
        super().gdo_create_form(form)

    def gdo_execute(self) -> GDT:
        return self.empty()
