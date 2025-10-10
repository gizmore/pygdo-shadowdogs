from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Bool import GDT_Bool
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class reset(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_Bool('confirm'))
        super().gdo_create_form(form)

    def gdo_execute(self) -> GDT:
        if self.param_value('confirm'):
            return self.reset()
        return self.msg('msg_sd_reset_confirm')

    def reset(self):
        if player := self.get_player():
            player.delete()
            return self.msg('msg_sd_reset')
        else:
            return self.err('err_sd_start_first')
