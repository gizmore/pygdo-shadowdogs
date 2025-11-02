from gdo.core.GDT_Repeat import GDT_Repeat
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class craft(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdcraft'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdcr'

    def sd_combat_seconds(self) -> int:
        self.get_source().sd_craft_time() + self.get_target().sd_craft_time()

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_TargetArg('item').inventory().not_null(),
            GDT_TargetArg('target').inventory().obstacles().not_null(),
        )
        super().gdo_create_form(form)

    def get_source(self) -> Item:
        return self.param_value('item')

    def get_targets(self) -> Item:
        return self.param_value('target')

    async def sd_execute(self):
        item = self.get_source()
        targets = self.get_targets()
        return await item.on_craft(targets)
