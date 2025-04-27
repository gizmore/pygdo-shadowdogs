from random import choice

from gdo.core.GDT_Select import GDT_Select
from gdo.core.GDT_String import GDT_String
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO
from gdo.shadowdogs.actions.Action import Action


class GDT_TargetArg(WithPlayerGDO, GDT_Select):

    _foes: bool
    _others: bool
    _friends: bool
    _obstacles: bool
    _default_room: bool

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_s()
        self.maxlen(96)
        self._foes = False
        self._others = False
        self._friends = False
        self._obstacles = False
        self._default_room = False

    ########
    # Opts #
    ########

    def players(self, players: bool = True):
        return self.friends(players).foes(players).others(players)

    def foes(self, foes: bool = True):
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

    #######
    # GDT #
    #######
    def get_value(self):
        value = super().get_value()
        if value is not None:
            return value
        if self._default_room:
            return self.get_party().get_location()
        return None

    def gdo_choices(self) -> dict:
        choices = {}
        if self._foes:
            for epl in self.get_enemy_party().members:
                choices[str(epl.party_pos)] = epl
        if self._friends:
            for pl in self.get_party().members:
                choices[pl.render_name()] = pl
        if self._obstacles and self.get_party().does(Action.INSIDE):
            self.get_location()

            thers:

        if self._friends: