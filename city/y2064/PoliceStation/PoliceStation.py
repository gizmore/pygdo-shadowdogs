from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.city.y2064.PoliceStation.locations.Exit import Exit
from gdo.shadowdogs.city.y2064.PoliceStation.locations.ComparisonRoom import ComparisonRoom
from gdo.shadowdogs.city.y2064.PoliceStation.locations.EvidenceRoom import EvidenceRoom
from gdo.shadowdogs.city.y2064.PoliceStation.locations.InterrogationRoom import InterrogationRoom
from gdo.shadowdogs.city.y2064.PoliceStation.locations.JailRoom import JailRoom
from gdo.shadowdogs.city.y2064.PoliceStation.locations.LockerRoom import LockerRoom
from gdo.shadowdogs.city.y2064.PoliceStation.locations.OfficeRoom import OfficeRoom
from gdo.shadowdogs.city.y2064.PoliceStation.locations.Reception import Reception
from gdo.shadowdogs.city.y2064.PoliceStation.locations.Toilets import Toilets
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location


class PoliceStation(City):

    def sd_square_km(self) -> int:
        return 1

    ComparisonRoom: ComparisonRoom = ComparisonRoom()
    EvidenceRoom: EvidenceRoom = EvidenceRoom()
    Exit: Exit = Exit()
    InterrogationRoom: InterrogationRoom = InterrogationRoom()
    JailRoom: JailRoom = JailRoom()
    LockerRoom: LockerRoom = LockerRoom()
    OfficeRoom: OfficeRoom = OfficeRoom()
    Reception: Reception = Reception()
    Toilets: Toilets = Toilets()

    LOCATIONS: list[Location] = [
        ComparisonRoom,
        EvidenceRoom,
        Exit,
        InterrogationRoom,
        JailRoom,
        LockerRoom,
        OfficeRoom,
        Reception,
        Toilets,
    ]

    NPCS: list[tuple[str,int]] = [
        ('peine_cop', 1000),
    ]

    def sd_npc_none_chance(self, party: 'SD_Party') -> int:
        return 100000
