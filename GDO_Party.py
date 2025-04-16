from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Util import Arrays
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Action import GDT_Action
from gdo.shadowdogs.GDT_Target import GDT_Target

from typing import TYPE_CHECKING

from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location

if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player
    from gdo.shadowdogs.actions.Action import Action


class GDO_Party(WithShadowFunc, GDO):

    members: list['GDO_Player']

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

    def get_action_name(self) -> str:
        return self.gdo_val('party_action')


    def is_action_over(self) -> bool:
        return self.get_eta() < self.mod_sd().cfg_time()

    def get_action(self) -> 'Action':
        return self.gdo_value('party_action')

    def get_eta(self) -> int:
        return self.gdo_value('party_eta')

    def do(self, action: str, target: str = None, eta: int = None):
        self.set_val('party_last_action', self.gdo_val('party_action'))
        self.set_val('party_last_target', self.gdo_val('party_target'))
        self.set_val('party_last_eta', self.gdo_val('party_eta')) # compute remaining seconds
        self.set_val('party_action', action)
        self.set_val('party_target', target if target else self.gdo_val('party_target'))
        self.set_val('party_eta', str(self.mod_sd().cfg_time() + eta) if eta else '0')
        return self.save()

    def resume(self):
        return self.do(
            self.gdo_val('party_last_action'),
            self.gdo_val('party_last_target'),
            self.gdo_val('party_last_eta'),
        )

    def join(self, player: 'GDO_Player'):
        if player in self.members:
            self.members.remove(player)
        self.members.append(player)
        player.save_vals({
            'p_party': self.get_id(),
            'p_joined': str(self.mod_sd().cfg_time()),
        })
        return self.with_fresh_positions()

    def with_fresh_positions(self):
        for n, player in enumerate(self.members):
            player.party_pos = n
        return self

    def kick(self, player: 'GDO_Player'):
        if player in self.members:
            self.members.remove(player)
        return self

    def tick(self):
        self.get_action().execute(self)
        return self

    def get_target(self) -> any:
        return self.gdo_value('party_target')

    def get_location(self) -> 'Location':
        return self.get_target()

    def get_city(self) -> 'City':
        return self.get_target()

    def get_target_string(self):
        return self.gdo_val('party_target')

    async def fight(self, party: 'GDO_Party'):
        self.do('fight', party.get_id())
        party.do('fight', self.get_id())
        await self.send_to_party(self, 'msg_sd_fight_started', (party.render_members(),))
        await self.send_to_party(party, 'msg_sd_fight_started', (self.render_members(),))
        for player in self.members:
            player.combat_stack.reset()
        for player in party.members:
            player.combat_stack.reset()
        return self

    def render_members(self) -> str:
        return Arrays.human_join([f"{p.party_pos}-{p.render_name()}" for p in self.members])
