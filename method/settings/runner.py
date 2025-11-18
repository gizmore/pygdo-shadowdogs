from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class runner(MethodSD):

    def gdo_has_permission(self, user: 'GDO_User'):
        if not super().gdo_has_permission(user):
            return False
        if self.get_player().gb('p_level') > Shadowdogs.RUNNING_LEVEL:
            self.err('err_sd_no_more_runner_mode')
            return False
        return True
