from gdo.shadowdogs.GDO_Player import GDO_Player


class WithShadowFunc:

    def get_player(self) -> 'GDO_Player':
        return GDO_Player.get_by_aid(self._env_user.get_id())

