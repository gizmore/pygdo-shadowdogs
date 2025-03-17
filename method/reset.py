from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Bool import GDT_Bool
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class reset(WithShadowFunc, Method):

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_Bool('confirm'),
        ]

    def gdo_execute(self) -> GDT:
        if self.param_value('confirm'):
            return self.reset()
        return self.msg('msg_sd_reset_confirm')

    def reset(self):
        self.get_player().delete()
        return self.msg('msg_sd_reset')

