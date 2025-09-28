from gdo.shadowdogs.city.y2064.Peine.quests.CivilService import CivilService
from gdo.shadowdogs.item.classes.usable.Email import Email


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle

class ArmyLetter(Email):
    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        await super().on_use(target)
        await CivilService.instance().accept()
