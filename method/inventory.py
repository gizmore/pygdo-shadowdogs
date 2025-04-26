from gdo.base.ResultArray import ResultArray
from gdo.base.Result import Result
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.table.MethodTable import MethodTable


class inventory(WithShadowMethod, MethodTable):

    def gdo_create_form(self, form: GDT_Form) -> None:
        super().gdo_create_form(form)

    def gdo_table_result(self) -> Result:
        return ResultArray(self.get_player().inventory, SD_Item.table())

    def form_submitted(self):
        pass
