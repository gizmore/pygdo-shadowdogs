from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class use(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sduse'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdu'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_ItemArg('item').obstacles().inventory().equipment().not_null(),
            GDT_TargetArg('target').me().obstacles().friends().foes().inventory().positional(),
        )
        super().gdo_create_form(form)

    def get_item(self) -> Item:
        return self.param_value('item')

    def get_target(self) -> SD_Player|Obstacle:
        return self.param_value('target')

    def sd_combat_seconds(self) -> float:
        return self.get_item().sd_use_time()

    async def sd_execute(self):
        await self.get_item().on_use(self.get_target())
        return self.empty()
