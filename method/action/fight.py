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
        party.do(Action.FIGHT, eparty.get_id())
        eparty.do(Action.FIGHT, party.get_id())
        self.send_to_party(party, 'msg_sd_encounter', (eparty.render_members(),))
        self.send_to_party(eparty, 'msg_sd_encounter', (party.render_members(),))
        return self.empty()
