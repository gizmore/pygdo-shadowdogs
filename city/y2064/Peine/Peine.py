from gdo.base.Util import Random
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
    Park: Park = Park()
    Police: Police = Police()
    Bank: Bank = Bank()
    CarRepairShop: CarRepairShop = CarRepairShop()
    Obi: Obi = Obi()

    LOCATIONS: list[Location] = [
        Alfred,
        Bank,
        CarRepairShop,
        GaragePub,
        GunzelinSchool,
        Home,
        Marketplace,
        Obi,
        SeniorHome,
        Jawoll,
        WaffenKief,
        Woods,
        TrainStation,
        Park,
        Police,
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

    async def sd_on_explore(self, party: 'SD_Party'):
        for member in party.members:
            if Random.mrand(0, 1000) < 1:
                await self.give_new_items(member, 'Bottle', 'explore', self.render_name())
        return self
