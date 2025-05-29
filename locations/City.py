from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.locations.Location import Location

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_Party import SD_Party


class City:

    LOCATIONS: list[Location] = []

    def sd_square_km(self) -> int:
        return 18

    def get_location(self, loc_str: str):
        matches = []
        for location in self.LOCATIONS:
            if loc_str in location.render_name():
                matches.append(location)
        if len(matches) == 0:
            raise ShadowdogsException('err_sd_no_match')
        if len(matches) == 1:
            return matches[0]
        raise ShadowdogsException('err_sd_much_matches')

    def get_name(self):
        return self.__class__.__name__

    def get_respawn_location(self, player: 'SD_Player') -> Location:
        from gdo.shadowdogs.engine.World import World
        return World.AmBauhof15.Bedroom

    def get_explore_eta(self, party: 'SD_Party') -> int:
        return 300 - party.gmin('p_qui')
