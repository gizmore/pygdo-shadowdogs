from gdo.form.MethodForm import MethodForm
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.shadowdogs.actions.Action import Action


class MethodSD(WithShadowMethod, MethodForm):

    def form_submitted(self):
        if self.sd_method_is_instant():
            return self.sd_execute()
        if self.get_party().does(Action.FIGHT):
            self.get_player().combat_stack.command = self

        return super().form_submitted()

    def sd_execute(self):
        return self.empty()
