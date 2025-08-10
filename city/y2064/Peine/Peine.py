from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.city.y2064.Peine.locations.Home import Home
from gdo.shadowdogs.city.y2064.Peine.locations.Marketplace import Marketplace
from gdo.shadowdogs.city.y2064.Peine.locations.SeniorHome import SeniorHome
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Peine(City):

    Marketplace: Marketplace = Marketplace()
    SeniorHome: SeniorHome = SeniorHome()
    Home: Home = Home()

    LOCATIONS: list[Location] = [
        Marketplace,
        SeniorHome,
        Home,
    ]

    def sd_npc_none_chance(self, party: 'SD_Party') -> int:
        return 1600

    NPCS: list[tuple[str, int]] = [
        ('lamer', 100)
    ]
