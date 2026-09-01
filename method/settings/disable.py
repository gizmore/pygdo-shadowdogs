from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDO_Permission import GDO_Permission
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class disable(WithShadowFunc, Method):
    """Disable Shadowdogs commands in the current channel.

    The two channel controls deliberately remain enabled, otherwise a channel
    could not be re-enabled without an administrator editing configuration.
    """

    def gdo_in_private(self) -> bool:
        return False

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sddisable'

    @classmethod
    def gdo_default_enabled_channel(cls) -> bool:
        return True

    def gdo_user_permission(self) -> str | None:
        return GDO_Permission.STAFF

    def gdo_execute(self) -> GDT:
        for method in self.mod_sd().get_methods():
            if method.__class__.__name__ not in ('enable', 'disable'):
                method.env_copy(self).save_config_channel('disabled', '1')
                # A successful permission check is cached by method/user.
                # Channel state just changed, so that cached success is stale.
                method.CACHE.pop(method.__class__, None)
        return self.msg('msg_sd_disabled')
