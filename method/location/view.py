from gdo.base.Render import Mode, Render
from gdo.base.Result import Result
from gdo.base.ResultArray import ResultArray
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Store import Store
from gdo.table.GDT_PageNum import GDT_PageNum
from gdo.table.MethodTable import MethodTable


class view(MethodSD, MethodTable):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdview'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdv'

    def sd_is_location_specific(self) -> bool:
        return True

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_PageNum('page').initial('1'),
        )
        super().gdo_create_form(form)

    def get_shop(self) -> Store|None:
        return self.get_location() if isinstance(self.get_location(), Store) else None

    def gdo_table_result(self) -> Result:
        items = self.get_shop().get_shop_items(self.get_player())
        return ResultArray(items, Item.table())

    def render_gdo(self, item: Item, mode: Mode) -> any:
        self._curr_table_row_id += 1
        return f"{Render.bold(str(self._curr_table_row_id), mode)}-{item.render_name()}({item.render_buy_price()})"

