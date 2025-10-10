from typing import TYPE_CHECKING

from gdo.shadowdogs.city.y2064.Peine.npcs.home.DejaVu import DejaVu
from gdo.shadowdogs.city.y2064.Peine.npcs.home.Lazer import Lazer
from gdo.shadowdogs.city.y2064.Peine.npcs.home.Mom import Mom
from gdo.shadowdogs.city.y2064.Peine.npcs.home.Theodor import Theodor
from gdo.shadowdogs.city.y2064.Peine.npcs.home.Thomas import Thomas
from gdo.shadowdogs.locations.Bedroom import Bedroom
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.Searchable import Searchable
from gdo.shadowdogs.obstacle.minigame.Computer import Computer
from gdo.shadowdogs.obstacle.minigame.tile.Vault import Vault

if TYPE_CHECKING:
    from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
    from gdo.shadowdogs.SD_Player import SD_Player

class Home(Bedroom,Location):

    GIVING: str = 'Jeans,Shoes,12xNuyen,ArmyLetter'

    NPCS: list['type[TalkingNPC]'] = [
        Mom,
        Lazer,
        Thomas,
        DejaVu,
        Theodor,
    ]

    OBSTACLES_INSIDE: list[Obstacle] = [
        Searchable('Fridge').giving('Coke,LargeBeer,Sandwich'),
        # Computer('PC').tile(Vault().password('gizmore', 4).giving('EmailArmy')),
    ]

    def sd_is_respawn(self, player: 'SD_Player') -> bool:
        return True
