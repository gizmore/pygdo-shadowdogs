from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.item.Item import Item


class Equipment(Item):

    def sd_inv_type(self) -> str:
        return GDT_Slot.INVENTORY
