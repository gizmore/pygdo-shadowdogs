from gdo.base.GDO import GDO
from gdo.base.Render import Mode
from gdo.core.GDT_Object import GDT_Object
from gdo.shadowdogs.SD_Location import SD_Location
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City
    from gdo.shadowdogs.SD_Place import SD_Place


class GDT_Location(WithPlayerGDO, GDT_Object):

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
        return self._gdo

    # def gdo(self, gdo: GDO):
    #     super().gdo(gdo)
    #     player = self.get_place().get_player()
    #     return self.player(player).city(self.get_party().get_city())

    def known(self, known: bool = True):
        self._known = known
        return self

    def same_city(self, same_city: bool = True):
        self._same_city = same_city
        return self

    def city(self, city: 'City'):
        self._city = city
        return self

    def render_cli(self, mode: Mode = Mode.HTML):
        return self.get_place().render_name()
