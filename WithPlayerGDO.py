from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.core.GDO_User import GDO_User
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.locations.Location import Location
    from gdo.shadowdogs.locations.City import City


class WithPlayerGDO:

    _player: 'SD_Player'

    def player(self, player: 'SD_Player'):
        self._player = player
        return self

    def get_user(self) -> 'GDO_User':
        return self.get_player().get_user()

    def get_player(self) -> 'SD_Player|None':
        if hasattr(self, '_player'):
            return self._player
        if hasattr(self, '_env_user'):
            if not self.__class__.World:
                from gdo.shadowdogs.engine.World import World
                self.__class__.World = World
            return self.__class__.World.get_player_for_user(self._env_user)
        return Shadowdogs.CURRENT_PLAYER

    def get_party(self) -> 'SD_Party':
        return self.get_player().get_party().player(self.get_player())

    def get_enemy_party(self) -> 'SD_Party':
        return self.get_party().get_target_party()

    def get_city(self) -> 'City':
        return self.get_party().get_city()

    def get_location(self) -> 'Location':
        return self.get_party().get_location()
