from gdo.core.GDT_Enum import GDT_Enum

from typing import TYPE_CHECKING

from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.locations.City import City


class GDT_City(WithShadowFunc, GDT_Enum):

    _all: bool
    _known: bool
    _default_current: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._all = False
        self._known = False
        self._default_current = False

    def all(self, all: bool = True):
        self._all = all
        return self

    def known(self, known: bool = True):
        self._known = known
        return self

    def default_current(self, default_current: bool=True):
        self._default_current = default_current
        return self

    def get_val(self):
        val = super().get_val()
        if val is None and self._default_current:
            return self.get_player().get_city().get_city_key()
        return val

    # def to_value(self, value: str):
    #     value = super().get_value()
    #     if value is None and self._default_current:
    #         return self.get_player().get_city()
    #     return value

    def gdo_choices(self) -> dict:
        if self._all:
            return self.all_city_choices()
        choices = {}
        player = self.get_player()
        world = player.get_party().get_world()
        for city in world.CITIES.values():
            if self.player_knows_city(player, city):
                choices[city.get_city_key()] = city
        return choices

    def player_knows_city(self, player: 'SD_Player', city: 'City') -> bool:
        from gdo.shadowdogs.SD_Place import SD_Place
        return SD_Place.table().select().join_object('kp_location').where(f'l_city="{city.get_location_key()}" AND kp_player={player.get_id()}').exec().fetch_val() is not None

    def all_city_choices(self) -> dict[str, 'City']:
        back = {}
        for world in self.world().WORLDS.values():
            for city in world.CITIES.values():
                back[city.get_city_key()] = city
        return back
