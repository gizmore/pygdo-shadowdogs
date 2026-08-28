from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodMove import MethodMove


class hunt(MethodMove):
    """Start following a player in the current city."""

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdhunt'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdh'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_Player('target').humans().not_null())
        super().gdo_create_form(form)

    def get_target_player(self) -> SD_Player:
        return self.param_value('target')

    async def sd_execute(self):
        target = self.get_target_player()
        party = self.get_party()
        location = target.get_party().get_location()
        if location is None:
            return self.err('err_sd_hunt_unavailable', (target.render_name(),))
        if target.get_city() is not party.get_city():
            return self.err('err_sd_hunt_city', (target.render_name(),))
        await party.do(Action.HUNT, str(target.get_id()), party.calc_goto_eta_s(location))
        return self.empty()
