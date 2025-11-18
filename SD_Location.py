from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name
from gdo.date.GDT_Created import GDT_Created

from typing import TYPE_CHECKING

from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_LocationVal import SD_LocationVal
    from gdo.shadowdogs.locations.Location import Location


class SD_Location(WithShadowFunc, GDO):

    SD_LocationVal = None

    def gdo_persistent(self) -> bool:
        return False

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('l_id'),
            GDT_Name('l_name').maxlen(128).ascii().case_s().not_null().pattern('/^[a-zA-Z][-._a-zA-Z0-9]$/'),
            GDT_City('l_city').all().not_null(),
            GDT_Created('l_created'),
        ]

    def get_location_key(self) -> str:
        return self.gdo_val('l_name')

    @classmethod
    def get_by_name(cls, name: str):
        return cls.table().get_by('l_name', name)

    def get_location(self) -> 'Location':
        return self.world().get_location(self.get_location_key())

    @classmethod
    def get_or_create(cls, location: 'Location'):
        key = location.get_location_key()
        if not (loc := cls.get_by_name(key)):
            loc = cls.blank({
                'l_name': key,
                'l_city': location.get_city().get_location_key(),
            }).insert()
        return loc

    def lv(self):
        if not self.__class__.SD_LocationVal:
            from gdo.shadowdogs.SD_LocationVal import SD_LocationVal
            self.__class__.SD_LocationVal = SD_LocationVal
        return self.__class__.SD_LocationVal

    def lv_get(self, key: str) -> str:
        return self.lv().table().select('lv_val').where(f"lv_player={self.get_player().get_id()} AND lv_location={self.get_id()} AND lv_key='{key}'").first().exec(False).fetch_val()

    def lv_set(self, key: str, val: str):
        self.lv().blank({
            'lv_player': self.get_player().get_id(),
            'lv_location': self.get_id(),
            'lv_key': key,
            'lv_val': val,
        }).soft_replace()
        return self
