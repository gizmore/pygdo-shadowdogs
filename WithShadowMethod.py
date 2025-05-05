from gdo.base.GDO import GDO
from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.actions.Action import Action


class WithShadowMethod(WithShadowFunc):
    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sd' + cls.__name__

    @classmethod
    def gdo_trig(cls) -> str:
        return cls.gdo_trigger()[0:4]

    def sd_is_item_specific(self) -> str:
        return GDO.EMPTY_STR

    def sd_is_location_specific(self) -> bool:
        return False

    def sd_location_actions(self) -> tuple[str]:
        return Action.INSIDE,

    def sd_requires_player(self) -> bool:
        from gdo.shadowdogs.engine.Loader import Loader
        Loader.load_user(self._env_user)
        return True

    def sd_requires_action(self) -> list[str] | None:
        return None

    def sd_method_is_instant(self) -> bool:
        return self.sd_combat_seconds() > 0

    def sd_combat_seconds(self) -> int:
        return 0

    def gdo_has_permission(self, user: 'GDO_User'):
        from gdo.shadowdogs.engine.World import World
        if not hasattr(self, '_player'):
            self.player(World.get_player_for_user(user))
        if self.sd_requires_player():
            if not self.get_player():
                self.err('err_sd_player_required')
                return False
        if item_name := self.sd_is_item_specific():
            if not self.get_player().inventory.has_item(item_name):
                self.err('err_sd_not_item', (item_name,))
                return False
        if self.sd_is_location_specific():
            if (self.gdo_trigger() not in self.get_location().sd_methods() or
                not self.get_party().does(*self.sd_location_actions())):
                self.err('err_sd_not_here')
                return False
        if actions := self.sd_requires_action():
            if self.get_party().get_action_name() not in actions:
                self.err('err_sd_not_now', ())
                return False
        return True

    def sd_execute(self):
        return self.gdo_execute()
    