from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class throw(MethodSD):

    @classmethod
    def sd_trigger(cls) -> str:
        return "sdthrow"

    @classmethod
    def sd_trig(cls) -> str:
        return "sdth"

    def sd_combat_seconds(self) -> float:
        return Shadowdogs.THROW_TIME_BASE - Shadowdogs.THROW_TTME_PER_QUICKNESS * self.get_player().g('p_qui')

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_TargetArg('target').foes(GDT_TargetArg.FOES_RANDOM).not_null().player(self.get_player()),
        )
        super().gdo_create_form(form)

    def sd_execute(self):
        pass
    