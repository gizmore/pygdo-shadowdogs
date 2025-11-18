from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.MethodSD import MethodSD


class part(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdpart"

    def gdo_create_form(self, form: GDT_Form) -> None:
        super().gdo_create_form(form)

    async def sd_execute(self):
        old_party = self.get_party()
        if len(old_party.members) == 1:
            return self.err('err_sd_not_in_party')
        old_party.kick(self.get_player())
        await self.send_to_party(old_party, 'msg_sd_player_left_party', (self.get_player().render_name(),))
        new_party = Factory.create_party(old_party.get_location())
        new_party.join_silent(self.get_player())
        return self.reply('msg_sd_parted')
