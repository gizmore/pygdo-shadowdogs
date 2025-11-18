from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.trains.Bum import Bum
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.locations.Railways import Railways
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class TrainStation(Railways):

    NPCS: 'list[type[TalkingNPC]]' = [
        Bum,
    ]

    GIVING: str = "Stone"

    def sd_methods(self) -> list[str]:
        return [
            'sdtravel',
            'sdsearch',
        ]

    def sd_travelt_targets(self, player: SD_Player) -> list[tuple[Location, int, int]]:
        targets = []
        party = player.get_party()
        if party.gmin('p_level') >= self.world().World2064.Oberg.MIN_LEVEL:
            targets.append((self.world().World2064.Oberg.BusStop, 10, Shadowdogs.SECONDS_PEINE_OBERG))
        if party.gmin('p_level') >= self.world().World2064.Nauen.MIN_LEVEL:
            targets.append((self.world().World2064.Nauen.TrainStation, 69, Shadowdogs.SECONDS_PEINE_NAUEN))
        targets.append()
        return  targets
