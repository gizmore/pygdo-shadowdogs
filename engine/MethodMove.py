from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.core.GDO_User import GDO_User


class MethodMove(MethodSD):

    def sd_is_leader_command(self) -> bool:
        return True

    def gdo_has_permission(self, user: 'GDO_User'):
        if not super().gdo_has_permission(user):
            return False
        player = self.get_player()
        overloaded = []
        for member in self.get_party().members:
            if member.cannot_move():
                overloaded.append(member)
        if overloaded:
            self.err('err_sd_player_required')
            return False
        return True
