from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDO_Player import GDO_Player
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.engine.MethodSD import MethodSD


class attack(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_TargetArg('target').foes().not_null())
        super().gdo_create_form(form)

    def get_target(self) -> GDO_Player:
        return self.param_value('target')

    def form_submitted(self):
        target = self.get_target()
        player = self.get_player()
        player.get_weapon().attack(target)
