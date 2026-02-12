from gdo.base.Util import Random
from gdo.shadowdogs.city.y2064.Peine.locations.CornerShop import CornerShop
from gdo.shadowdogs.city.y2064.Peine.locations.Drugstore import Drugstore
from gdo.shadowdogs.city.y2064.Peine.locations.bank.Bank import Bank
from gdo.shadowdogs.city.y2064.Peine.locations.car_repair.CarRepairShop import CarRepairShop
from gdo.shadowdogs.city.y2064.Peine.locations.obi.Obi import Obi
from gdo.shadowdogs.city.y2064.Peine.locations.park.Park import Park
from gdo.shadowdogs.city.y2064.Peine.locations.trains.TrainStation import TrainStation
from gdo.shadowdogs.city.y2064.Peine.locations.alfred.Alfred import Alfred
from gdo.shadowdogs.city.y2064.Peine.locations.gunzelin.GunzelinSchool import GunzelinSchool
from gdo.shadowdogs.city.y2064.Peine.locations.home.Home import Home
from gdo.shadowdogs.city.y2064.Peine.locations.market.Marketplace import Marketplace
from gdo.shadowdogs.city.y2064.Peine.locations.garage.GaragePub import GaragePub
from gdo.shadowdogs.city.y2064.Peine.locations.seniorhome.SeniorHome import SeniorHome
from gdo.shadowdogs.city.y2064.Peine.locations.Jawoll import Jawoll
from gdo.shadowdogs.city.y2064.Peine.locations.waffenkief.WaffenKief import WaffenKief
from gdo.shadowdogs.city.y2064.Peine.locations.woods.Woods import Woods
from gdo.shadowdogs.city.y2064.Peine.locations.police.Police import Police
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class Peine(City):

    Alfred: Alfred = Alfred()
    Bank: Bank = Bank()
    CarRepairShop: CarRepairShop = CarRepairShop()
    CornerShop: CornerShop = CornerShop()
    Drugstore: Drugstore = Drugstore()
    GaragePub: GaragePub = GaragePub()
    GunzelinSchool: GunzelinSchool = GunzelinSchool()
    Home: Home = Home()
    Jawoll: Jawoll = Jawoll()
    Marketplace: Marketplace = Marketplace()
    Obi: Obi = Obi()
    Park: Park = Park()
    Police: Police = Police()
    SeniorHome: SeniorHome = SeniorHome()
    TrainStation: TrainStation = TrainStation()
    WaffenKief: WaffenKief = WaffenKief()
    Woods: Woods = Woods()

    LOCATIONS: list[Location] = [
        Alfred,
        Bank,
        CarRepairShop,
        CornerShop,
        Drugstore,
        GaragePub,
        GunzelinSchool,
        Home,
        Jawoll,
        Marketplace,
        Obi,
        Park,
        Police,
        SeniorHome,
        TrainStation,
        WaffenKief,
        Woods,
    ]

    NPCS: list[tuple[str, int]] = [
        ('lamer', 450),
        ('haider', 350),
        ('noob', 250),
        ('gangster', 250),
    ]

    def sd_square_km(self) -> int:
        return 19

    def sd_npc_none_chance(self, party: 'SD_Party') -> int:
        return 100_000

    def sd_npc_explore_level_gap(self, party: 'SD_Party') -> int:
        return 0

    async def sd_on_explore(self, party: 'SD_Party'):
        for member in party.members:
            if Random.mrand(0, 10000) < 1:
                await self.give_new_items(member, 'Bottle', 'explore', self.render_name())
        return self
