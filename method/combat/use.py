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
        item = self.get_item()
        target = self.get_target()
        if not item.sd_can_target() and target:
            return self.err('err_sd_use_not_on_target', (item.render_name_wc(),))
        if target:
            if not item.sd_can_use_on_friend() and target.is_friend():
                return self.err('err_sd_use_not_on_friend', (item.render_name_wc(),))
            if not item.sd_can_use_on_foe() and target.is_foe():
                return self.err('err_sd_use_not_on_foe', (item.render_name_wc(),))
        elif not item.sd_can_use_on_self():
            return self.err('err_sd_use_not_on_self', (item.render_name_wc(),))
        await item.on_use(target)
        return self.empty()
