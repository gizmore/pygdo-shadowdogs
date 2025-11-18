from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class WithShadowMethod(WithShadowFunc):

    World = None

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sd' + cls.__name__

    @classmethod
    def gdo_trig(cls) -> str:
        return cls.gdo_trigger()[0:4]

    def sd_is_leader_command(self) -> bool:
        return False

    def sd_is_item_specific(self) -> bool:
        return False

    def sd_requires_item_name(self) -> list[str]:
        return GDT.EMPTY_LIST

    def sd_requires_item_klass(self) -> list[str]:
        return GDT.EMPTY_LIST

    def sd_is_location_specific(self) -> bool:
        return False

    def sd_location_actions(self) -> tuple[str]:
        return (Action.INSIDE,)

    def sd_requires_player(self) -> bool:
        if not self._player:
            from gdo.shadowdogs.engine.Loader import Loader
            Loader.load_user(self._env_user)
        return True

    def sd_requires_action(self) -> list[str] | None:
        return None

    def sd_method_is_instant(self) -> bool:
        return self.sd_combat_seconds() <= 0

    def sd_combat_seconds(self) -> int:
        return 0

    def gdo_before_execute(self):
        player = Shadowdogs.CURRENT_PLAYER
        if self._env_user.is_human():
            player = self.world().get_player_for_user(self._env_user)
            Shadowdogs.CURRENT_PLAYER = player
        self.player(player)

    def gdo_has_permission(self, user: 'GDO_User'):
        if self.sd_requires_player():
            if not self.get_player():
                self.err('err_sd_player_required')
                return False
        if klass := self.sd_requires_item_klass():
            found = False
            for itm in self._player.all_equipment():
                if itm.dm('klass') == klass:
                    found = True
                    break
            if not found:
                self.err('err_sd_item_klass_required', (klass, ))
                return False
        if self.sd_is_item_specific():
            if not self.gdo_trigger() in self.get_player().get_sd_methods():
                self.err('err_sd_missing_item')
                return False
        if self.sd_is_location_specific():
            if (self.gdo_trigger() not in self.get_location().sd_methods() or
                not self.get_party().does(*self.sd_location_actions())):
                self.err('err_sd_not_here')
                return False
        if actions := self.sd_requires_action():
            if self.get_party().get_action_name() not in actions:
                self.err('err_sd_not_now')
                return False
        return True

    def parameters(self, reset: bool = False) -> dict[str,GDT]:
        params = super().parameters(reset)
        for gdt in params:
            if hasattr(gdt, 'player'):
                gdt.player(self.get_player())
        return params


    def sd_execute(self):
        return self.gdo_execute()
    