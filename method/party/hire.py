from gdo.core.GDT_UInt import GDT_UInt
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.npcs.Hireling import Hireling


class hire(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdhire'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdhi'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_TargetArg('npc').others().not_null().positional(),
            GDT_UInt('nuyen').not_null().positional().initial('0'),
        )
        super().gdo_create_form(form)

    def get_target(self) -> Hireling:
        return self.param_value('npc')

    async def sd_execute(self):
        hireling = self.get_target().player(self.get_player())
        await hireling.on_hire(self.get_player(), self.param_value('nuyen'))
        return self.empty()
