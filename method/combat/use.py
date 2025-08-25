from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class use(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').inventory().equipment().not_null(),
            GDT_TargetArg('target').me().obstacles().friends().foes().positional(),
        )
        super().gdo_create_form(form)

    def get_sd_item(self) -> SD_Item:
        return self.param_value('item')

    def get_item(self) -> Item:
        return self.get_sd_item().itm()

    def get_target(self) -> SD_Player:
        return self.param_value('target')

    def sd_combat_seconds(self) -> float:
        return self.get_item().itm().sd_attack_time()

    async def form_submitted(self):
        await self.get_item().on_use(self.get_target())
        return self.empty()
