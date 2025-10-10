from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD


class join(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdjoin"

    @classmethod
    def gdo_trig(cls) -> str:
        return "sdj"

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Player('player').humans().nearby().not_null()
        )
        super().gdo_create_form(form)

    def get_target_player(self) -> SD_Player:
        return self.param_value('player')

    async def sd_execute(self):
        old_party = self.get_party()
        if len(old_party.members) == 1:
            old_party.delete()
        player = self.get_target_player()
        new_party = player.get_party()
        new_party.join_silent(self.get_player())
        await self.send_to_party(new_party, 'msg_sd_player_joined', (self.get_player().render_name(),))
        return self.empty()
