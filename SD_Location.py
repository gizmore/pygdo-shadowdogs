from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name
from gdo.date.GDT_Created import GDT_Created

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.locations.Location import Location



class SD_Location(GDO):

    def gdo_persistent(self) -> bool:
        return False

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('l_id'),
            GDT_Name('l_name').maxlen(128).ascii().case_s().not_null().pattern('/^[a-zA-Z][-._a-zA-Z0-9]$/'),
            GDT_Created('l_created'),
        ]

    @classmethod
    def get_by_name(cls, name: str):
        return cls.table().get_by('l_name', name)

    @classmethod
    def get_or_create(cls, location: 'Location'):
        key = location.get_location_key()
        if not (loc := cls.get_by_name(key)):
            loc = cls.blank({
                'l_name': key,
            }).insert()
        return loc
