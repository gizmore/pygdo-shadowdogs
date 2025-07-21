from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.engine.WithProbability import WithProbability
from gdo.shadowdogs.locations.Location import Location

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_Party import SD_Party


class City(WithShadowFunc):

    LOCATIONS: list[Location] = []

    def get_name(self):
        return self.__class__.__name__

    def sd_square_km(self) -> int:
        return 25

    ############
    # Location #
    ############

    def get_location_by_str(self, loc_str: str):
        matches = []
        for location in self.LOCATIONS:
            if loc_str in location.render_name():
                matches.append(location)
        if len(matches) == 0:
            raise ShadowdogsException('err_sd_no_match')
        if len(matches) == 1:
            return matches[0]
        raise ShadowdogsException('err_sd_much_matches')

    def get_respawn_location(self, player: 'SD_Player') -> Location:
        from gdo.shadowdogs.city.y2064.World2064 import World2064
        return World2064.Peine.Home

    ###########
    # Explore #
    ###########

    def explore_non_chance(self, party: 'SD_Party') -> int:
        return self.sd_square_km() * Shadowdogs.EXPLORE_NONE_CHANCE_PER_SQKM

    def get_explore_eta(self, party: 'SD_Party') -> int:
        return self.sd_square_km() * Shadowdogs.EXPLORE_ETA_PER_SQKM - party.gmin('p_qui') * Shadowdogs.EXPLORE_ETA_BONUS_PER_QUICKNESS

    def on_explored(self, party: 'SD_Party'):
        items = []
        for location in self.LOCATIONS:
            items.append((location, location.explore_find_chance(party)))
        location = WithProbability.probable_item(items, self.explore_non_chance(party))
        if location:
            self.give_kp(party.get_leader(), location)
        elif items:
            self.send_to_party(party, 'msg_found_no_location')
        else:
            self.send_to_party(party, 'msg_no_more_locations')
        return self
