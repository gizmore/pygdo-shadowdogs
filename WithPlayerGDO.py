from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.locations.Location import Location
    from gdo.shadowdogs.locations.City import City


class WithPlayerGDO:

    _player: 'SD_Player'

    def player(self, player: 'SD_Player'):
        self._player = player
        return self

    def get_player(self) -> 'SD_Player':
        return self._player

    def get_party(self) -> 'SD_Party':
        return self.get_player().get_party()

    def get_enemy_party(self) -> 'SD_Party':
        return self.get_player().get_party().get_target_party()

    def get_city(self) -> 'City':
        return self.get_party().get_city()

    def get_location(self) -> 'Location':
        return self.get_party().get_location()
