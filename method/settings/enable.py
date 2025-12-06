from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class enable(WithShadowFunc, Method):

    def gdo_in_private(self) -> bool:
        return False

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdenable'

    @classmethod
    def gdo_default_enabled_channel(cls) -> bool:
        return True

    def gdo_execute(self) -> GDT:
        for method in self.mod_sd().get_methods():
            method.env_copy(self).save_config_channel('disabled', '0')
        return self.msg('msg_sd_enabled')
