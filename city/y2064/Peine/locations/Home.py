from typing import TYPE_CHECKING

from gdo.shadowdogs.city.y2064.Peine.npcs.home.Lazer import Lazer
from gdo.shadowdogs.city.y2064.Peine.npcs.home.Mom import Mom
from gdo.shadowdogs.city.y2064.Peine.npcs.home.Thomas import Thomas
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Obstacle import Obstacle
from gdo.shadowdogs.obstacle.Searchable import Searchable
from gdo.shadowdogs.obstacle.minigame.Computer import Computer

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_NPC import SD_NPC

class Home(Location):

    GIVING: str = 'Pullover,Jeans,Shoes,MobilePhone,12xNuyen'

    NPCS: list['SD_NPC'] = [
        Mom(),
        Lazer(),
        Thomas(),
    ]

    OBSTACLES_INSIDE: list[Obstacle] = [
        Searchable('Fridge').giving('Coke,LargeBeer'),
        Computer('PC').vault('Email1'),
    ]

