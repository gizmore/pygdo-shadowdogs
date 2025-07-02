from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.obstacle.minigame.Computer import Computer
from gdo.shadowdogs.obstacle.minigame.Map import Map


class Executable(Item):

    def get_computer(self) -> Computer:
        return self.get_party().get_target()

    def get_computer_map(self) -> Map:
        return self.get_computer().get_map(self.get_player())
