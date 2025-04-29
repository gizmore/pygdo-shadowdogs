from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Util import Arrays
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Action import GDT_Action
from gdo.shadowdogs.GDT_Target import GDT_Target

from typing import TYPE_CHECKING, Self, Iterator

from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.actions.Action import Action


class SD_Party(WithShadowFunc, GDO):

    members: list['SD_Player']

    __slots__ = (
        'members',
    )

    def __init__(self):
        super().__init__()
        self.members = []

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('party_id'),
            GDT_Action('party_action').not_null(),
            GDT_Target('party_target').not_null(),
            GDT_UInt('party_eta').not_null(),
            GDT_Action('party_last_action'),
            GDT_Target('party_last_target'),
            GDT_UInt('party_last_eta'),
            GDT_Created('party_created'),
        ]

    async def do(self, action: str, target: str = None, eta: int = 0):
        if last_eta := self.gdo_value('party_eta'):
            last_eta = last_eta - self.get_time()
        self.save_vals({
            'party_last_action': self.gdo_val('party_action'),
            'party_last_target': self.gdo_val('party_target'),
            'party_last_eta': str(last_eta),
            'party_action': action,
            'party_target': target if target else self.gdo_val('party_target'),
            'party_eta': str(self.get_time() + eta) if eta else '0',
        })
        await self.get_action().player(self.members[0]).on_start(self)
        return self

    async def resume(self):
        if eta := self.gdo_value('party_last_eta'):
            eta += self.mod_sd().cfg_time()
        return self.do(
            self.gdo_val('party_last_action'),
            self.gdo_val('party_last_target'),
            eta,
        )

    ###########
    # Members #
    ###########

    def join(self, player: 'SD_Player'):
        if player in self.members:
            self.members.remove(player)
        self.members.append(player)
        player.save_vals({
            'p_party': self.get_id(),
            'p_joined': str(self.get_time()),
        })
        return self.with_fresh_positions()

    def with_fresh_positions(self):
        for n, player in enumerate(self.members):
            player.party_pos = n + 1
        return self

    def kick(self, player: 'SD_Player'):
        if player in self.members:
            self.members.remove(player)
        return self

    ##########
    # Target #
    ##########

    def players_nearby(self) -> Iterator['SD_Player']:
        action = self.get_action_name()
        for epa in Shadowdogs.PARTIES.values():
            if epa.get_location(action) == self.get_location(action):
                yield from epa.members

    def get_target_string(self):
        return self.gdo_val('party_target')

    def get_target(self) -> any:
        return self.gdo_value('party_target')

    def get_last_target(self) -> any:
        return self.gdo_value('party_last_target')

    def get_target_party(self) -> 'SD_Party|None':
        from gdo.shadowdogs.actions.Action import Action
        if self.does(Action.FIGHT, Action.TALK):
            return self.get_target()

    def get_city(self) -> City|None:
        if city := self.get_city_from_target(self.get_target()):
            return city
        return self.get_city_from_target(self.get_last_target())

    def get_city_from_target(self, target: City|Location|Self) -> City|None:
        if isinstance(target, City):
            return target
        if isinstance(target, Location):
            return target.get_city()

    def get_location(self, action: str = None) -> 'Location|None':
        if action is not None:
            if self.get_action_name() != action:
                return None
        from gdo.shadowdogs.actions.Action import Action
        if self.does(Action.FIGHT, Action.TALK):
            if target := self.get_last_target():
                if isinstance(target, Location):
                    return target
        if self.does(Action.INSIDE, Action.OUTSIDE, Action.SLEEP):
            return self.get_target()
        return None

    ##########
    # Action #
    ##########
    async def tick(self):
        if self.is_action_over():
            await self.get_action().on_completed(self)
        else:
            await self.get_action().execute(self)
        return self

    def get_action_name(self) -> str:
        return self.gdo_val('party_action')

    def get_last_action_name(self) -> str:
        return self.gdo_val('party_last_action')

    def get_action(self) -> 'Action':
        return self.gdo_value('party_action')

    def get_eta(self) -> int:
        return self.gdo_value('party_eta')

    def get_eta_s(self) -> int:
         time = self.get_eta()
         return time - self.get_time() if time else 0

    def calc_goto_eta_s(self, location: Location) -> int:
        city = location.get_city()
        sqkm = city.sd_square_km()
        nloc = len(city.LOCATIONS)
        return round((sqkm ** 3) / nloc)

    def is_action_over(self) -> bool:
        return self.get_eta() <= self.get_time()

    def does(self, *actions: str) -> bool:
        return self.get_action_name() in actions

    def was(self, *actions: str) -> bool:
        return self.get_last_action_name() in actions

    async def fight(self, party: 'SD_Party'):
        from gdo.shadowdogs.actions.Action import Action
        await self.do(Action.FIGHT, party.get_id())
        await party.do(Action.FIGHT, self.get_id())
        for player in self.members:
            player.combat_stack.reset()
        for player in party.members:
            player.combat_stack.reset()
        return self

    ##########
    # Render #
    ##########

    def render_members(self) -> str:
        return Arrays.human_join([f"{p.party_pos}-{p.render_name()}" for p in self.members])
