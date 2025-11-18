from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.item.classes.Equipment import Equipment


class Cyberware(Equipment):

   def sd_inv_type(self) -> str:
        return GDT_Slot.CYBERWARE
