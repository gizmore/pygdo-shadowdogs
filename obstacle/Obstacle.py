from gdo.shadowdogs.SD_ObstacleVal import SD_ObstacleVal
from gdo.shadowdogs.item.Item import Item


class Obstacle(Item):

    OBSTACLES: dict[str, 'Obstacle'] = {}

    def __init__(self, name: str):
        super().__init__(name)
        klass = self.__class__.__name__
        if klass in self.OBSTACLES:
            raise RuntimeError(f"Obstacle {klass} already defined")
        self.OBSTACLES[klass] = self

    def sd_commands(self) -> list[str]:
        return [
            'sdsearch',
        ]

    async def on_search(self):
        await self.send_to_player(self.get_player(), 'sd_on_search_nothing')

    ########
    # Data #
    #########

    def gobs(self, key: str) -> str:
        return SD_ObstacleVal.table().get_by_id(self.get_player().get_id(), self.__class__.__name__, key).gdo_val('ov_val')

    def sobs(self, key: str, val: str):
        SD_ObstacleVal.blank({
            'ov_player': self.get_player().get_id(),
            'ov_obstacle': self.__class__.__name__,
            'ov_key': key,
            'ov_val': val,
        }).soft_replace()
        return self
