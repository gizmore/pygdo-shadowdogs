from gdo.base.Application import Application
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Util import Arrays, Random
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from gdo.date.Time import Time
from gdo.shadowdogs.GDT_Action import GDT_Action
from gdo.shadowdogs.GDT_LootMode import GDT_LootMode
from gdo.shadowdogs.GDT_Target import GDT_Target

from typing import TYPE_CHECKING, Iterator

from gdo.shadowdogs.GDT_World import GDT_World
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations.Location import Location

if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City
    from gdo.shadowdogs.engine.World import World
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.actions.Action import Action
    from gdo.shadowdogs.engine.WorldBase import WorldBase


class SD_Party(WithShadowFunc, GDO):

    World = None
    members: list['SD_Player']
    combat_direction: bool

    __slots__ = (
        'members',
        'combat_direction',
    )

    def __init__(self):
        super().__init__()
        self.members = []
        self.combat_direction = True # positive

    def __repr__(self):
        return f"Party({self.get_id()}):({self.render_members()}) {self.get_action_name()} {self.get_target_string()}"

    def gdo_ipc(self) -> bool:
        return False

    def gdo_columns(self) -> list[GDT]:
         return [
            GDT_AutoInc('party_id'),
            GDT_Action('party_action').not_null(),
            GDT_Target('party_target').not_null(),
            GDT_UInt('party_eta').not_null(),
            GDT_Action('party_last_action'),
            GDT_Target('party_last_target').last_target(),
            GDT_UInt('party_last_eta'),
            GDT_World('party_world').not_null().initial('y2064'),
            GDT_UInt('party_kills').not_null().initial('0'),
            GDT_LootMode('party_loot_mode').not_null().initial(GDT_LootMode.KILLER),
            GDT_Created('party_created'),
        ]

    #######
    # GDO #
    #######
    def delete(self):
        if self.get_id() in Shadowdogs.PARTIES:
            del Shadowdogs.PARTIES[self.get_id()]
        return super().delete()

    ##########
    # Action #
    ##########

    async def do(self, action: str, target: str = None, eta: int = 0):
        if last_eta := self.gdo_value('party_eta'):
            last_eta = max(0, last_eta - self.get_time())
        self.save_vals({
            'party_last_action': self.gdo_val('party_action'),
            'party_last_target': self.gdo_val('party_target'),
            'party_last_eta': str(last_eta),
            'party_action': action,
            'party_target': target if target else self.gdo_val('party_target'),
            'party_eta': str(self.get_time() + eta) if eta else '0',
        })
        if self.members:
            await self.get_action().player(self.members[0]).on_start(self)
        Application.EVENTS.publish(f'on_sd_{self.get_action_name()}_start', self)
        return self

    async def resume(self):
        return await self.do(
            self.gdo_val('party_last_action'),
            self.gdo_val('party_last_target'),
            self.gdo_value('party_last_eta'),
        )

    def all_busy(self, seconds: int):
        for player in self.members:
            player.busy(seconds)
        return self

    ###########
    # Members #
    ###########

    def is_empty(self) -> bool:
        return len(self.members) == 0

    def get_leader(self) -> 'SD_Player':
        return self.members[0] if self.members else None

    def last_member(self) -> 'SD_Player':
        return self.members[-1]

    async def join(self, player: 'SD_Player'):
        if player in self.members:
            self.members.remove(player)
        self.members.append(player)
        player.save_vals({
            'p_party': self.get_id(),
            'p_joined': str(self.get_time()),
        })
        await self.send_to_party(self, 'msg_sd_joined_party', (player.render_name(),))
        return self.with_fresh_positions()

    def join_silent(self, player: 'SD_Player'):
        if player in self.members:
            self.members.remove(player)
        self.members.append(player)
        player.save_vals({
            'p_party': self.get_id(),
            'p_joined': str(Application.TIME),
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

    ###########
    # Min/Max #
    ###########

    def gmin(self, field: str) -> int:
        return self.get_min(field, 'g')

    def gbmin(self, field: str) -> int:
        return self.get_min(field, 'gb')

    def get_min(self, field: str, func: str) -> int:
        min = 65536
        for player in self.members:
            v = getattr(player, func)(field)
            min = v if v < min else min
        return min

    def gmax(self, field: str) -> int:
        return self.get_max(field, 'g')

    def gbmax(self, field: str) -> int:
        return self.get_max(field, 'gb')

    def get_max(self, field: str, func: str) -> int:
        max = 0
        for player in self.members:
            v = getattr(player, func)(field)
            max = v if v > max else max
        return max

    #########
    # Mount #
    #########

    def get_mount_speed(self) -> int | None:
        without_mount = []
        with_mount = []
        seats = 0
        min_speed = 100
        for member in self.members:
            if mount := member.get_mount():
                with_mount.append(member)
                seats += mount.get_seats()
                min_speed = min(min_speed, mount.get_real_speed())
            else:
                without_mount.append(member)
        if len(without_mount) > seats or min_speed == 0:
            return None
        return min_speed

    ##########
    # Target #
    ##########

    def other_players(self, player: 'SD_Player' = None, own_members: bool=True):
        """
        Get current other players a player sees.
        """
        from gdo.shadowdogs.actions.Action import Action
        yield from self.players_nearby(player)
        if self.get_action_name() == Action.INSIDE:
            for npc in self.get_location(Action.INSIDE).npcs(player or self.get_leader()):
                yield npc
        if self.get_action_name() == Action.OUTSIDE:
            for npc in self.get_location(Action.OUTSIDE).npcs(player or self.get_leader()):
                yield npc
        if self.get_action_name() == Action.FIGHT or self.get_action_name() == Action.TALK:
            yield from self.members
            yield from self.get_enemy_party().members

    def players_nearby(self, exclude: 'SD_Player' = None) -> Iterator['SD_Player']:
        action = self.get_action_name()
        for epa in Shadowdogs.PARTIES.values():
            if epa.get_location(action) == self.get_location(action):
                for player in epa.members:
                    if player != exclude:
                        yield player

    def get_target_string(self):
        return self.gdo_val('party_target')

    def get_target(self) -> any:
        target = self.gdo_value('party_target')
        return target.player(self.get_leader()) if target else None

    def get_last_target_string(self) -> str:
        return self.gdo_val('party_last_target')

    def get_last_target(self) -> any:
        return self.gdo_value('party_last_target')

    def get_target_party(self) -> 'SD_Party|None':
        from gdo.shadowdogs.actions.Action import Action
        if self.does(Action.FIGHT, Action.TALK):
            return self.get_target()
        return None

    def random_member(self) -> 'SD_Player|None':
        return Random.list_item(self.members)

    def get_city(self) -> 'City|None':
        if not self.get_target_string().isdigit():
            if city := self.get_city_from_target(self.get_target()):
                return city
        else:
            return self.get_city_from_target(self.get_last_target())
        return None

    def get_world(self) -> 'WorldBase':
        if not self.__class__.World:
            from gdo.shadowdogs.engine.World import World
            self.__class__.World = World
        return self.__class__.World.WORLDS.get(self.gdo_val('party_world'))

    @staticmethod
    def get_city_from_target(target) -> 'City|None':
        from gdo.shadowdogs.locations.City import City
        if isinstance(target, City):
            return target
        if isinstance(target, Location):
            return target.get_city()
        return None

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
    async def digesting(self):
        for player in self.members:
            await player.digesting()

    async def tick(self):
        if self.is_action_over():
            await self.get_action().on_completed(self)
            Application.EVENTS.publish(f'on_sd_{self.get_action_name()}_over', self)
        else:
            await self.get_action().execute(self)
        return self

    def get_action_name(self) -> str:
        return self.gdo_val('party_action')

    def get_last_action_name(self) -> str:
        return self.gdo_val('party_last_action')

    def get_action(self) -> 'Action':
        return self.gdo_value('party_action').player(self.get_leader())

    def get_last_action(self) -> 'Action':
        return self.gdo_value('party_last_action').player(self.get_leader())

    def get_eta(self) -> int:
        return self.gdo_value('party_eta')

    def get_eta_s(self) -> int:
         time = self.get_eta()
         return time - self.get_time() if time else 0

    def calc_goto_eta_s(self, location: Location) -> int:
        city = location.get_city()
        sqkm = city.sd_square_km()
        # nloc = len(city.LOCATIONS)
        return int(round((sqkm ** Shadowdogs.GOTO_SECONDS_POW)))

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
            player.combat_stack().reset()
            player.distance = Random.mrand(2, Shadowdogs.MAX_DISTANCE)
        for player in party.members:
            player.combat_stack().reset()
            player.distance = Random.mrand(-Shadowdogs.MAX_DISTANCE, -2)
        self.combat_diraction = True
        party.combat_direction = False
        return self

    ###################
    # Enter and Leave #
    ###################


    ##########
    # Render #
    ##########

    def render_members(self) -> str:
        return Arrays.human_join([f"{p.party_pos}-{p.render_name()}" for p in self.members])

    def combat_diraction_sign(self) -> int:
        return 1 if self.combat_diraction else -1

    def render_busy(self) -> str:
        return self.t('sd_busy', (Time.human_duration(self.get_eta_s()),))

