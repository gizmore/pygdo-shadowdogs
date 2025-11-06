from typing import TYPE_CHECKING

from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.DejaVu import DejaVu
from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.Lazer import Lazer
from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.Mom import Mom
from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.Theodor import Theodor
from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.Thomas import Thomas
from gdo.shadowdogs.locations.Bedroom import Bedroom
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Bed import Bed
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.Searchable import Searchable
from gdo.shadowdogs.obstacle.Sink import Sink

if TYPE_CHECKING:
    from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
    from gdo.shadowdogs.SD_Player import SD_Player

class Home(Bedroom,Location):

    GIVING: str = 'Jeans,Shoes,12xNuyen,ArmyLetter,Bottle'

    NPCS: list['type[TalkingNPC]'] = [
        Mom,
        Lazer,
        Thomas,
        DejaVu,
        Theodor,
    ]

    OBSTACLES_INSIDE: list[Obstacle] = [
        Searchable('fridge').giving('2xCoke,2xLargeBeer,2xSandwich'),
        Bed('bed'),
        Sink('sink'),
        # Computer('PC').tile(Vault().password('gizmore', 4).giving('EmailArmy')),
    ]

    def sd_is_respawn(self, player: 'SD_Player') -> bool:
        return True
