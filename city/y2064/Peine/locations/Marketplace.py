from gdo.shadowdogs.city.y2064.Peine.npcs.Moellring import Moellring
from gdo.shadowdogs.city.y2064.Peine.quests.Etablisment import Etablisment
from gdo.shadowdogs.locations.Bedroom import Bedroom
from gdo.shadowdogs.locations.Location import Location

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC

class Marketplace(Bedroom, Location):

    NPCS: list['type[TalkingNPC]'] = [
        Moellring,
        # Hempel,
    ]

    def sd_methods(self) -> list[str]:
        if Etablisment.instance().is_accomplished():
            return [
                'sdsleep',
            ]
        return []
