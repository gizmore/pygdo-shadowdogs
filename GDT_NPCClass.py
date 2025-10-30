from gdo.core.GDT_Enum import GDT_Enum
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class GDT_NPCClass(GDT_Enum):

    TALKING_NPCS: dict[str,type['TalkingNPC']] = {}

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.maxlen(255)
        self.case_s()

    def gdo_choices(self) -> dict:
        from gdo.shadowdogs.npcs.npcs import npcs
        from gdo.shadowdogs.engine.Loader import Loader
        Loader.init_npc_classes()
        c = { data['klass'].fqcn(): klass for klass, data in npcs.NPCS.items() }
        c.update(self.TALKING_NPCS)
        return c
