from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.engine.MethodSD import MethodSD


class fight(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdfight'

    def gdo_has_permission(self, user: 'GDO_User'):
        return self.get_player(user).get_party().get_action_name() == 'talk'

    def form_submitted(self):
        party = self.get_party()
        eparty = party.get_target()
        party.do('fight', eparty.get_id())
        eparty.do('fight', party.get_id())
        self.send_to_party(party, 'msg_sd_encounter', (eparty.render_members(),))
        self.send_to_party(eparty, 'msg_sd_encounter', (party.render_members(),))
        return self.empty()
