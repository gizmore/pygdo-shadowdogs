from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.Item import Item


class mopop(MethodSD):

    def sd_requires_mount(self) -> bool:
        return True

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'mopop'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').mount().not_null(),
        )
        super().gdo_create_form(form)

    def get_item(self) -> Item:
        return self.param_value('item')

    def sd_combat_seconds(self) -> int:
        return int(self.get_item().get_weight() * Shadowdogs.GIVE_SECONDS_PER_WEIGHT)

    def sd_execute(self):
        item = self.get_item().slot(GDT_Slot.INVENTORY).save()
        mount = self.get_player().get_mount()
        return self.reply('msg_sd_put_out_of_mount', (item.render_name(), mount.render_name()))
    