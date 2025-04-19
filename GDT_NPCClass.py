from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.npcs.npcs import npcs


class GDT_NPCClass(GDT_Enum):

    def gdo_choices(self) -> dict:
        return { name.lower(): name for name in npcs.NPCS }
