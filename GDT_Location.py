from gdo.base.GDO import GDO
from gdo.core.GDT_Object import GDT_Object
from gdo.shadowdogs.SD_Location import SD_Location
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City


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

    def gdo(self, gdo: GDO):
        super().gdo(gdo)
        return self.city(self.get_party().get_city())

    def known(self, known: bool = True):
        self._known = known
        return self

    def same_city(self, same_city: bool = True):
        self._same_city = same_city
        return self

    def city(self, city: 'City'):
        self._city = city
        return self
