from typing import TYPE_CHECKING

from gdo.shadowdogs.city.y2064.Peine.npcs.home.DejaVu import DejaVu
from gdo.shadowdogs.city.y2064.Peine.npcs.home.Lazer import Lazer
from gdo.shadowdogs.city.y2064.Peine.npcs.home.Mom import Mom
from gdo.shadowdogs.city.y2064.Peine.npcs.home.Thomas import Thomas
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.Searchable import Searchable
from gdo.shadowdogs.obstacle.minigame.Computer import Computer
from gdo.shadowdogs.obstacle.minigame.tile.Vault import Vault

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_NPC import SD_NPC
    from gdo.shadowdogs.SD_Player import SD_Player

class Home(Location):

    GIVING: str = 'Pullover,Jeans,Shoes,12xNuyen,GizmoreNote'

    NPCS: list['SD_NPC'] = [
        Mom(),
        Lazer(),
        Thomas(),
        DejaVu(),
    ]

    OBSTACLES_INSIDE: list[Obstacle] = [
        Searchable('Fridge').giving('Coke,LargeBeer'),
        Computer('PC').tile(Vault().password('gizmore', 4).giving('EmailArmy')),
    ]

    def npcs(cls, player: 'SD_Player') -> 'list[SD_NPC]':
        return cls.NPCS
