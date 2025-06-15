from gdo.shadowdogs.SD_ObstacleVal import SD_ObstacleVal
from gdo.shadowdogs.item.Item import Item


class Obstacle(Item):

    def on_search(self):
        self.send_to_player(self.get_player(), 'sd_on_search_nothing')

    ########
    # Data #
    #########

    def gobs(self, key: str) -> str:
        return SD_ObstacleVal.table().get_by_id(self.get_player().get_id(), self._name, key).gdo_val('ov_val')

    def sobs(self, key: str, val: str):
        SD_ObstacleVal.blank({
            'ov_player': self.get_player().get_id(),
            'ov_obstacle': self._name,
            'ov_key': key,
            'ov_val': val,
        }).soft_replace()
        return self
