from gdo.core.GDO_User import GDO_User
from gdo.form.MethodForm import MethodForm
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class MethodSD(WithShadowFunc, MethodForm):

    def sd_is_location_specific(self) -> bool:
        return False

    def sd_requires_player(self) -> bool:
        return True

    def sd_requires_action(self) -> list[str]|None:
        return None

    def sd_combat_seconds(self) -> int:
        return 0

    def gdo_has_permission(self, user: 'GDO_User'):
        if self.sd_requires_player():
            if not self.get_player():
                self.err('err_sd_player_required')
                return False
        if self.sd_is_location_specific():
            if self.gdo_trigger() not in self.get_location().sd_methods():
                self.err('err_sd_not_here')
                return False
        if actions := self.sd_requires_action():
            if self.get_party().get_action_name() not in actions:
                self.err('err_sd_not_now')
                return False
        return True
