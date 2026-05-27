from typing import TYPE_CHECKING

from gdo.shadowdogs.city.y2064.Brunswick.locations.hospital.Hospital import Hospital
from gdo.shadowdogs.city.y2064.Brunswick.locations.smithers.Smithers import Smithers
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.city.y2064.Brunswick.locations.headshop.Headshop import Headshop
from gdo.shadowdogs.city.y2064.Brunswick.locations.trains.Railways import Railways
from gdo.shadowdogs.city.y2064.Brunswick.locations.school.ITSchool import ITSchool

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class Brunswick(City):

    Headshop: Headshop = Headshop()
    Hospital: Hospital = Hospital()
    ITSchool: ITSchool = ITSchool()
    Smithers: Smithers = Smithers()
    Railways: Railways = Railways()

    LOCATIONS: list[Location] = [
        Headshop,
        Hospital,
        ITSchool,
        Smithers,
        Railways,
    ]

    NPCS: list[tuple[str, int]] = [
        ('gangster', 100),
        ('goblin', 100),
        ('ork', 100),
    ]
