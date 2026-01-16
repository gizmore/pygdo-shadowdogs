from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class fight(MethodSD):

    def sd_is_leader_command(self) -> bool:
        return True

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdfight'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdf'

    def gdo_has_permission(self, user: 'GDO_User'):
        return self.get_player(user).get_party().does(Action.TALK)

    def form_submitted(self):
        party = self.get_party()
        eparty = party.get_target()
        party.fight(eparty)
        return self.empty()
