from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.obstacle.minigame.Computer import Computer
from gdo.shadowdogs.obstacle.minigame.Map import Map


class Executable(Item):

    def sd_inv_type(self) -> str:
        return GDT_Slot.CYBERDECK

    def get_computer(self) -> Computer:
        return self.get_party().get_target()

    def get_computer_map(self) -> Map:
        return self.get_computer().get_map(self.get_player())

    def get_slot(self) -> str:
        return 'cyberdeck'
