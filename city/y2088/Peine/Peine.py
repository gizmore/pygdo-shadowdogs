from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.city.y2064.Peine.locations.home.Home import Home
from gdo.shadowdogs.city.y2064.Peine.locations.market.Marketplace import Marketplace
from gdo.shadowdogs.city.y2064.Peine.locations.garage.GaragePub import GaragePub
from gdo.shadowdogs.city.y2064.Peine.locations.seniorhome.SeniorHome import SeniorHome
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Peine(City):

    Home: Home = Home()
    Marketplace: Marketplace = Marketplace()
    SeniorHome: SeniorHome = SeniorHome()
    GaragePub: GaragePub = GaragePub()

    LOCATIONS: list[Location] = [
        Marketplace,
        SeniorHome,
        Home,
        GaragePub,
    ]

    NPCS: list[tuple[str, int]] = [
        ('lamer', 100),
        ('haider', 100),
        ('noob', 100),
        ('gangster', 100),
    ]

    def sd_square_km(self) -> int:
        return 40

    def sd_npc_none_chance(self, party: 'SD_Party') -> int:
        return 500000

    def sd_npc_explore_level_gap(self, party: 'SD_Party') -> int:
        return 0
