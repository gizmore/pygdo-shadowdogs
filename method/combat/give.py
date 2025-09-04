from gdo.core.GDT_UInt import GDT_UInt
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class give(MethodSD):

    def sd_combat_seconds(self) -> int:
        return self.get_item().get_weight() // Shadowdogs,GIVE_SECONDS_PER_WEIGHT

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Player('to').npcs().nearby_players().not_null(),
            GDT_ItemArg('item').inventory().not_null(),
            GDT_UInt('count').initial('1').positional(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> SD_Player:
        return self.param_value('to')

    def get_item(self) -> SD_Item:
        return self.param_value('item')

    def sd_execute(self):
        to = self.get_target()
        item = self.get_item()
        count = self.param_value('count')
        new_item = to.inventory.remove_item(item.render_name(), count)
        self.give_item(to, new_item, 'give', self.get_player().render_name())

