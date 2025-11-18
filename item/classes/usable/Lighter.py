from gdo.shadowdogs.item.classes.Usable import Usable

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Lighter(Usable):

    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        pass
