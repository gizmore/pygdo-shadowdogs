from gdo.core.GDO_User import GDO_User
from gdo.form.MethodForm import MethodForm
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod


class MethodSD(WithShadowMethod, MethodForm):

    def sd_method_is_instant(self) -> bool:
        return True

    def form_submitted(self):
        if self.sd_method_is_instant():
            return self.sd_execute()
        self.get_player().combat_stack.push(self)
        return self.empty()

    def sd_execute(self):
        return self.empty()
