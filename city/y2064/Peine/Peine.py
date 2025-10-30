from gdo.shadowdogs.city.y2064.Peine.locations.TrainStation import TrainStation
from gdo.shadowdogs.city.y2064.Peine.locations.alfred.Alfred import Alfred
from gdo.shadowdogs.city.y2064.Peine.locations.gunzelin.GunzelinSchool import GunzelinSchool
from gdo.shadowdogs.city.y2064.Peine.locations.home.Home import Home
from gdo.shadowdogs.city.y2064.Peine.locations.market.Marketplace import Marketplace
from gdo.shadowdogs.city.y2064.Peine.locations.garage.GaragePub import GaragePub
from gdo.shadowdogs.city.y2064.Peine.locations.seniorhome.SeniorHome import SeniorHome
from gdo.shadowdogs.city.y2064.Peine.locations.Jawoll import Jawoll
from gdo.shadowdogs.city.y2064.Peine.locations.waffenkief.WaffenKief import WaffenKief
from gdo.shadowdogs.city.y2064.Peine.locations.woods.Woods import Woods
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class Peine(City):

    Home: Home = Home()
    Marketplace: Marketplace = Marketplace()
    SeniorHome: SeniorHome = SeniorHome()
    GaragePub: GaragePub = GaragePub()
    Jawoll: Jawoll = Jawoll()
    WaffenKief: WaffenKief = WaffenKief()
    GunzelinSchool: GunzelinSchool = GunzelinSchool()
    Alfred: Alfred = Alfred()
    Woods: Woods = Woods()
    TrainStation: TrainStation = TrainStation()

    LOCATIONS: list[Location] = [
        Marketplace,
        SeniorHome,
        Home,
        GaragePub,
        Jawoll,
        WaffenKief,
        GunzelinSchool,
        Alfred,
        Woods,
        TrainStation,
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
