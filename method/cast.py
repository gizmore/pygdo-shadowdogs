from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Spell import GDT_Spell
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.engine.MethodSD import MethodSD


class cast(MethodSD):

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdc'

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdcast'

    def sd_method_is_instant(self) -> bool:
        return False

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Spell('spell').not_null(),
            GDT_TargetArg('target').friends().foes().others().positional(),
        )
        super().gdo_create_form(form)

    def sd_execute(self):
        pass
