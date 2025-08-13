from gdo.base.Util import Random
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.engine.WithProbability import WithProbability
from gdo.shadowdogs.locations.Location import Location

from typing import TYPE_CHECKING

from gdo.shadowdogs.npcs.npcs import npcs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_Party import SD_Party


class City(WithShadowFunc):

    LOCATIONS: list[Location] = []

    NPCS: list[tuple[str,int]] = []

    def get_name(self):
        return self.__class__.__name__

    def sd_square_km(self) -> int:
        return 25

    #######
    # NPC #
    #######

    def sd_npc_max_encounter(self, party: 'SD_Party') -> int:
        return Random.mrand(1, 1 + len(party.members))

    def sd_npc_none_chance(self, party: 'SD_Party') -> int:
        return 65535

    def sd_npc_explore_level_gap(self, party: 'SD_Party') -> int:
        return 8

    def get_npc_chances(self, party: 'SD_Party', level_gap: int):
        chances = []
        pl = party.gbmax('p_level')
        for klass, prob in self.NPCS:
            nl = npcs.NPCS[klass].get('p_level', 1)
            if nl - level_gap <= pl:
                chances.append((klass, prob))
        return chances

    ############
    # Location #
    ############
    def get_location_key(self) -> str:
       return self.get_city_key()

    def get_city_key(self) -> str:
        m = self.__class__.__module__.split('.')
        return m[3] + "." + m[-1]

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

    async def on_explore(self, party: 'SD_Party'):
        from gdo.shadowdogs.engine.Factory import Factory
        encounters = []
        npcs = self.get_npc_chances(party, self.sd_npc_explore_level_gap(party))
        for i in range(self.sd_npc_max_encounter(party)):
            if npc := WithProbability.probable_item(npcs, self.sd_npc_none_chance(party)):
                encounters.append(npc)
        if encounters:
            ep = await Factory.create_default_npcs(party.get_city(), *encounters)
            await ep.do(Action.OUTSIDE, party.get_city().get_location_key())
            await ep.fight(party)

    async def on_explored(self, party: 'SD_Party'):
        items = []
        for location in self.LOCATIONS:
            items.append((location, location.explore_find_chance(party)))
        location = WithProbability.probable_item(items, self.explore_non_chance(party))
        if location:
            await self.give_kp(party.get_leader(), location)
            await party.do(Action.OUTSIDE, location.get_location_key())
        elif items:
            await self.send_to_party(party, 'msg_found_no_location')
            await party.do(Action.OUTSIDE, party.get_city().get_location_key())
        else:
            await self.send_to_party(party, 'msg_no_more_locations')
            await party.do(Action.OUTSIDE, party.get_city().get_location_key())
        return self
