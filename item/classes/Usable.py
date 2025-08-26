from gdo.base.Exceptions import GDOException
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Usable(Item):

    def sd_commands(self) -> list[str]:
        return [
            'sduse',
        ]

    def sd_use_time(self) -> int:
        return 0

    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        raise GDOException('err_not_implemented')

    def get_default_count(self) -> int:
        return self.dmi('package', 1)
