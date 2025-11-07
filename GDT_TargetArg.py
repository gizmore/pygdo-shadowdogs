from random import choice

from gdo.core.GDT_Select import GDT_Select
from gdo.core.GDT_String import GDT_String
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO
from gdo.shadowdogs.actions.Action import Action


class GDT_TargetArg(WithPlayerGDO, GDT_Select):

    FOES_RANDOM = 2
    FOES_ENABLED = 1

    _me: bool
    _foes: int
    _others: bool
    _friends: bool
    _obstacles: bool
    _default_room: bool
    _inventory: bool

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_s()
        self.maxlen(96)
        self._me = False
        self._foes = 0
        self._others = False
        self._friends = False
        self._obstacles = False
        self._default_room = False
        self._inventory = False

    ########
    # Opts #
    ########

    def players(self, players: bool = True):
        return self.me().friends(players).foes(players).others(players)

    def me(self, me: bool = True):
        self._me = me
        return self

    def foes(self, foes: int = 1):
        self._foes = foes
        return self

    def others(self, others: bool = True):
        self._others = others
        return self

    def friends(self, friends: bool = True):
        self._friends = friends
        return self

    def obstacles(self, obstacles: bool = True):
        self._obstacles = obstacles
        return self

    def default_room(self, default_room: bool = True):
        self._default_room = default_room
        return self

    def inventory(self, inventory: bool = True):
        self._inventory = inventory
        return self

    #######
    # GDT #
    #######
    def to_value(self, val: str):
        if val:
            return super().to_value(val) or self.get_enemy_party().random_member()
        if self._foes == self.FOES_RANDOM:
            return self.get_enemy_party().random_member()
        if self._default_room:
            return self.get_party().get_location()
        return None


    def get_value(self):
        value = super().get_value()
        if value is not None:
            return value
        return None

    def gdo_choices(self) -> dict:
        choices = {}
        player = self.get_player()
        party = self.get_party()
        if self._me:
            choices[player.get_name()] = player
        if self._foes:
            if party.does(Action.FIGHT):
                for epl in self.get_enemy_party().members:
                    choices[str(epl.party_pos)] = epl
        if self._friends:
            for pl in self.get_party().members:
                choices[pl.get_name()] = pl
        if self._obstacles:
            for obstacle in self.get_location().obstacles(party.get_action_name(), player):
                choices[obstacle.render_name()] = obstacle
        if self._others:
            for pl in party.players_nearby():
                choices[pl.get_name()] = pl
            if location := self.get_location():
                for npc in location.get_npcs(player):
                    choices[npc.render_name()] = npc
        if self._inventory:
            for item in player.inventory:
                choices[item.render_name()] = item
        return choices
