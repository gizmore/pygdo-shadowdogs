from gdo.core.GDO_Permission import GDO_Permission
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_Enum import GDT_Enum
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Action import GDT_Action
from gdo.shadowdogs.GDT_Location import GDT_Location
from gdo.shadowdogs.GDT_LocationTarget import GDT_LocationTarget
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Location import SD_Location
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.locations.Location import Location


class gml(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdgml'

    def gdo_user_permission(self) -> str | None:
        return GDO_Permission.ADMIN

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Bool('learn').initial('1'),
            GDT_Player('player').humans().online().not_null(),
            GDT_Action('action').not_null(),
            GDT_LocationTarget('location').not_null(),
        )
        super().gdo_create_form(form)

    def get_target_player(self) -> SD_Player:
        return self.param_value('player')

    def get_target_action(self) -> Action:
        return self.param_value('action')

    def get_target_location(self) -> Location:
        return self.param_value('location')

    def should_learn(self) -> bool:
        return self.param_value('learn')

    async def sd_execute(self):
        player = self.get_target_player()
        party = player.get_party()
        action = self.get_target_action()
        location = self.get_target_location()
        await party.do(action.get_name(), location.get_location_key())
        await self.send_to_party(party, '%s', (action.render_action(party),))
        if self.should_learn():
            await self.give_kp(player, location)
        return self.reply('msg_sd_gml', (party.render_members(), action.render_name(), location.render_name()))
