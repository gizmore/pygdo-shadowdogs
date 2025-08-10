from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.WithGDO import WithGDO
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO


class GDT_City(WithPlayerGDO, GDT_Enum):

    _known: bool
    _default_current: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._known = False
        self._default_current = False

    def known(self, known: bool = True):
        self._known = known
        return self

    def default_current(self, default_current: bool=True):
        self._default_current = default_current
        return self

    def get_value(self):
        val = super().get_value()
        if val is None and self._default_current:
            return self.get_player().get_city()
        return val

    def gdo_choices(self) -> dict:
        choices = {}
        player = self.get_player()
        world = player.get_party().get_world()
        for city in world.CITIES:
            if self.player_knows_city(player, city):
                choices[city.get_location_key()] = city
        return choices

    def player_knows_city(self, player, city):
        return True

