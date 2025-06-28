from gdo.shadowdogs.SD_ObstacleVal import SD_ObstacleVal
from gdo.shadowdogs.item.Item import Item


class Obstacle(Item):

    OBSTACLES: dict[str, 'Obstacle'] = {}

    _obstacle_id: str

    @classmethod
    def get_by_obstacle_id(cls, obstacle_id: str):
        return cls.OBSTACLES.get(obstacle_id)

    def __init__(self, name: str):
        super().__init__(name)
        self._obstacle_id = name

    def obstacle_id(self, obstacle_id: str):
        self._obstacle_id = obstacle_id
        self.OBSTACLES[obstacle_id] = self
        return self

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
        return SD_ObstacleVal.table().get_by_id(self.get_player().get_id(), self._obstacle_id, key).gdo_val('ov_val')

    def sobs(self, key: str, val: str):
        SD_ObstacleVal.blank({
            'ov_player': self.get_player().get_id(),
            'ov_obstacle': self._obstacle_id,
            'ov_key': key,
            'ov_val': val,
        }).soft_replace()
        return self
