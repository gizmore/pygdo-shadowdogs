from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class runner(MethodSD):

    def gdo_has_permission(self, user: 'GDO_User'):
        if not super().gdo_has_permission(user):
            return False
        if self.get_player().gb('p_level') > Shadowdogs.RUNNING_LEVEL:
            return False
        return True

