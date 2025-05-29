from gdo.base.Trans import t
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_QuestDone import SD_QuestDone
from gdo.shadowdogs.city.AmBauhof15.obstacles.Computer1 import Computer1
from gdo.shadowdogs.engine.WithComputer import WithComputer
from gdo.shadowdogs.locations.Bedroom import Bedroom as BedroomBase
from gdo.shadowdogs.obstacle.Bed import Bed
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Bedroom(WithComputer, BedroomBase):
    OBSTACLES: list[Obstacle] = [
        Bed('Bed'),
        Computer1('Computer'),
    ]

    async def on_search(self, player: SD_Player):
        quest = SD_QuestDone.for_player('Connection', player)
        if not quest.is_accepted():
            await self.give_new_item(player, 'MobilePhone', 1, 'search', t('bedroom'))
            await self.send_to_player(player, 'sdq001_mobile_found')
            await quest.accept()

    async def on_hack(self, player: SD_Player, dir):
        pass
