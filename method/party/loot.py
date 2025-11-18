from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_LootMode import GDT_LootMode
from gdo.shadowdogs.engine.MethodSD import MethodSD


class loot(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdloot'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdlo'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_LootMode('mode').not_null(),)
        super().gdo_create_form(form)

    def sd_execute(self):
        self.get_party().save_val('party_loot', self.param_val('mode'))
        return self.msg('msg_sd_party_loot', (self.parameter('mode').render(),))
