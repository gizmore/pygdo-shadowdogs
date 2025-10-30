from gdo.core.GDT_UInt import GDT_UInt
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.npcs.Hireling import Hireling


class hire(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'hire'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'hi'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_TargetArg('npc').others().not_null().positional(),
            # GDT_UInt('nuyen').not_null().positional().initial('100'),
        )
        super().gdo_create_form(form)

    def get_target(self) -> Hireling:
        return self.param_value('npc')

    def sd_execute(self):
        hireling = self.get_target().player(self.get_player())
        hireling.on_hire()
        return self.empty()
