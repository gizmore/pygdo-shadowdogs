from gdo.shadowdogs.city.y2064.Peine.locations.Marketplace import Marketplace
from gdo.shadowdogs.city.y2064.Peine.locations.SeniorHome import SeniorHome
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class Peine(City):

    Marketplace: Marketplace = Marketplace()
    SeniorHome: SeniorHome = SeniorHome()

    LOCATIONS: list[Location] = [
        Marketplace,
        SeniorHome,
    ]
