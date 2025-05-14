from gdo.core.GDT_Enum import GDT_Enum


class GDT_NPCClass(GDT_Enum):

    def gdo_choices(self) -> dict:
        from gdo.shadowdogs.npcs.npcs import npcs
        return { name.lower(): name for name in npcs.NPCS }
