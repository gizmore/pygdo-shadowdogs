from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class heal(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdheal'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdhe'

    def sd_is_location_specific(self) -> bool:
        return True

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
        )
        super().gdo_create_form(form)

    def get_item(self) -> Item:
        return self.param_value('item')

    def get_amount(self) -> int:
        return self.param_value('amount')

    async def sd_execute(self) -> GDT:
        return await self.get_location().on_heal(self.get_player())
