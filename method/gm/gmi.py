from gdo.core.GDO_Permission import GDO_Permission
from gdo.core.GDT_Repeat import GDT_Repeat
from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.core.GDT_String import GDT_String
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.MethodSD import MethodSD


class gmi(MethodSD):
    """
    GM Item - Give a freshly created item to a player.
    Example: $gmi gizmo Club_of_str:8
    Example: $gmi gizmo Club_of_adonis
    """

    def gdo_user_permission(self) -> str | None:
        return GDO_Permission.ADMIN

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Player('target').online().not_null(),
            GDT_String('item_name').not_null(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> SD_Player:
        return self.param_value('target')

    async def form_submitted(self):
        player = self.get_target()
        item_name = self.param_val('item_name')
        item = Factory.create_item_gmi(item_name)
        await self.give_item(player, item, 'gmi', self.get_player().render_name())
        player.modify_all()
        return self.msg('msg_sd_gmi_success', (item.render_name(), player.render_name()))
