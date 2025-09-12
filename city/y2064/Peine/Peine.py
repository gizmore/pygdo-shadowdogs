from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.city.y2064.Peine.locations import WaffenKief
from gdo.shadowdogs.city.y2064.Peine.locations.Home import Home
from gdo.shadowdogs.city.y2064.Peine.locations.Marketplace import Marketplace
from gdo.shadowdogs.city.y2064.Peine.locations.GaragePub import GaragePub
from gdo.shadowdogs.city.y2064.Peine.locations.SeniorHome import SeniorHome
from gdo.shadowdogs.city.y2064.Peine.locations.Jawoll import Jawoll
from gdo.shadowdogs.city.y2064.Peine.locations.WaffenKief import WaffenKief
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Peine(City):

    Home: Home = Home()
    Marketplace: Marketplace = Marketplace()
    SeniorHome: SeniorHome = SeniorHome()
    GaragePub: GaragePub = GaragePub()
    Jawoll: Jawoll = Jawoll()
    WaffenKief: WaffenKief = WaffenKief()

    LOCATIONS: list[Location] = [
        Marketplace,
        SeniorHome,
        Home,
        GaragePub,
        Jawoll,
        WaffenKief,
    ]

    NPCS: list[tuple[str, int]] = [
        ('lamer', Shadowdogs.NPC_ENCOUNTER_CHANCE),
        ('haider', 100),
        ('noob', 100),
        ('gangster', 100),
    ]

    def sd_square_km(self) -> int:
        return 40

    def sd_npc_none_chance(self, party: 'SD_Party') -> int:
        return 100000

    def sd_npc_explore_level_gap(self, party: 'SD_Party') -> int:
        return 0
