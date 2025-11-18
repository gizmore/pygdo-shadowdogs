from typing import Generator

from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations.City import City



class WorldBase(WithShadowFunc):

    CITIES: dict[str,City] = {
    }

    def __repr__(self):
        return self.__class__.__name__

    def get_parties(self) -> Generator[SD_Party, None, None]:
        for party in Shadowdogs.PARTIES.values():
            if party.get_world() is self:
                yield party

    def get_players(self) -> Generator[SD_Player, None, None]:
        for party in self.get_parties():
            yield from party.members

    def render_name(self):
        return self.__class__.__name__
