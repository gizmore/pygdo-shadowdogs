from functools import lru_cache

from gdo.base.Trans import t
from gdo.base.Util import Random
from gdo.shadowdogs.SD_Place import SD_Place
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.engine.WithProbability import WithProbability
from gdo.shadowdogs.locations.Location import Location

from typing import TYPE_CHECKING, Generator

from gdo.shadowdogs.npcs.npcs import npcs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_Party import SD_Party


class City(WithShadowFunc):

    LOCATIONS: list[Location] = []

    NPCS: list[tuple[str,int]] = []

    def get_name(self):
        return self.__class__.__name__

    def render_name(self):
        return t(self.__class__.__name__.replace('.', '_'))

    def sd_square_km(self) -> int:
        return 25

    def __repr__(self):
        return f"{self.__class__.__module__.split('.')[3]}.{self.__class__.__name__}"

    #######
    # NPC #
    #######

    def sd_npc_max_encounters(self, party: 'SD_Party') -> int:
        return Random.mrand(Shadowdogs.MIN_ENCOUNTERS, Shadowdogs.MAX_ENCOUNTER_BASE + len(party.members) + party.get_max('p_level', 'g') // Shadowdogs.LEVELS_PER_MAX_ENCOUNTER)

    def sd_npc_none_chance(self, party: 'SD_Party') -> int:
        return Shadowdogs.NPC_ENCOUNTER_NONE_CHANCE

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

    @lru_cache
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

    def get_respawn_location(self, player: 'SD_Player') -> Location|None:
        for place in SD_Place.query_for_player(player).order('kp_found DESC').exec():
            if place.get_location().sd_is_respawn(player):
                return place.get_location()
        return None

    ###########
    # Explore #
    ###########

    def explore_non_chance(self, party: 'SD_Party') -> int:
        return self.sd_square_km() * Shadowdogs.EXPLORE_NONE_CHANCE_PER_SQKM

    def get_explore_eta(self, party: 'SD_Party') -> int:
        base = self.sd_square_km() * Shadowdogs.EXPLORE_ETA_PER_SQKM
        if speed := party.get_mount_speed():
            base -= speed * Shadowdogs.EXPLORE_ETA_BONUS_PER_SPEED
        else:
            base -= party.gmin('p_qui') * Shadowdogs.EXPLORE_ETA_BONUS_PER_QUICKNESS
        return int(max(Shadowdogs.EXPLORE_ETA_MIN, base))

    async def on_explore(self, party: 'SD_Party'):
        if await self.on_explore_mobs(party):
            return self
        if await self.on_meet_humans(party):
            return self
        if await self.sd_on_explore(party):
            return self
        return self

    async def sd_on_explore(self, party: 'SD_Party'):
        return self

    async def on_explore_mobs(self, party: 'SD_Party'):
        encounters = []
        npcs = self.get_npc_chances(party, self.sd_npc_explore_level_gap(party))
        for i in range(self.sd_npc_max_encounters(party)):
            if npc := WithProbability.probable_item(npcs, self.sd_npc_none_chance(party)):
                encounters.append(npc)
        if encounters:
            ep = await self.factory().create_default_npcs(party.get_city(), *encounters)
            await ep.do(Action.OUTSIDE, party.get_city().get_location_key())
            await ep.fight(party)

    async def on_meet_humans(self, party: 'SD_Party'):
        for ep in self.parties_doing((Action.EXPLORE, Action.GOTO)):
            if ep is not party:
                chance_total = Shadowdogs.MEET_CHANCE_TOTAL / (self.sd_square_km() * Shadowdogs.MEET_CHANCE_DIV_PER_SQKM)
                if Random.mrand(0, int(chance_total)) < Shadowdogs.MEET_CHANCE_MEET:
                   await ep.fight(party)

    async def on_explored(self, party: 'SD_Party'):
        items = []
        for location in self.LOCATIONS:
            items.append((location, location.explore_find_chance(party)))
        location = WithProbability.probable_item(items, self.explore_non_chance(party))
        if location:
            await party.do(Action.OUTSIDE, location.get_location_key())
            await self.give_party_kp(party, location)
        elif items:
            await self.send_to_party(party, 'msg_found_no_location')
            await party.do(Action.OUTSIDE, party.get_city().get_location_key())
        else:
            await self.send_to_party(party, 'msg_no_more_locations')
            await party.do(Action.OUTSIDE, party.get_city().get_location_key())
        return self

    def parties_doing(self, actions: tuple[str,...]) -> Generator['SD_Party', None, None]:
        for party in Shadowdogs.PARTIES.values():
            if party.get_action_name() in actions:
                yield party
