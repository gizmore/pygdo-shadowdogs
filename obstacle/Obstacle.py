from gdo.shadowdogs.SD_ObstacleVal import SD_ObstacleVal
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item


class Obstacle(Item):

    def __init__(self, name: str = None):
        super().__init__()
        self.location = None
        self.fill_defaults()
        self._name = name
        self._vals = {
            'item_name': name,
            'item_count': '1',
        }

    def sd_commands(self) -> list[str]:
        return [
            'sdsearch',
        ]

    async def on_search(self, player: SD_Player):
        await self.send_to_player(player, 'sd_on_search_nothing')

    def gdo_can_persist(self) -> bool:
        return False


    ########
    # Data #
    #########

    def gobs(self, key: str) -> str|None:
        if v := SD_ObstacleVal.table().get_by_id(self.get_player().get_id(), self.location.get_location_id(), self.__class__.__name__, key):
            return v.gdo_val('ov_val')
        return None

    def sobs(self, key: str, val: str):
        SD_ObstacleVal.blank({
            'ov_player': self.get_player().get_id(),
            'ov_location': self.location.get_location_id(),
            'ov_obstacle': self.__class__.__name__,
            'ov_key': key,
            'ov_val': val,
        }).soft_replace()
        return self
