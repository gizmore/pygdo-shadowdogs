from gdo.base.GDO import GDO
from gdo.base.Render import Mode
from gdo.core.GDT_Object import GDT_Object
from gdo.shadowdogs.SD_Location import SD_Location
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO

from typing import TYPE_CHECKING

from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.World import World

if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City
    from gdo.shadowdogs.SD_Place import SD_Place


class GDT_LocationTarget(WithShadowFunc, GDT_Object):

    _known: bool
    _same_city: bool
    _city: 'City|None'

    def __init__(self, name: str):
        super().__init__(name)
        self.table(SD_Location.table())
        self._known = False
        self._same_city = False
        self._city = None

    def get_place(self) -> 'SD_Place':
        return self.get_value()

    # def gdo(self, gdo: GDO):
    #     super().gdo(gdo)
    #     player = self.get_place().get_player()
    #     return self.player(player).city(self.get_party().get_city())

    def query_gdos(self, val: str) -> list[GDO]:
        city, locstr = (val.lower().split('.', 1) + [None])[:2]
        if not locstr:
            locstr = city
            city = self.get_city()
        else:
            cities = World.get_city_by_abbrev(self.get_player(), city)
            if len(cities) == 0:
                return self.EMPTY_LIST
            elif len(cities) > 1:
                self.error('err_too_many')
                return cities
            else:
                city = cities[0]
        back = []
        for location in city.LOCATIONS:
            if locstr in location.render_name().lower():
                if self._known and not self.get_player().has_kp(location):
                    continue
                if self._same_city and location.get_city() is not city:
                    continue
                if self._city and location.get_city() is not city:
                    continue
                back.append(location)
        return back

    def known(self, known: bool = True):
        self._known = known
        return self

    def same_city(self, same_city: bool = True):
        self._same_city = same_city
        return self

    def city(self, city: 'City'):
        self._city = city
        return self

    def render_cli(self, mode: Mode = Mode.render_html):
        return self.get_place().render_name()
