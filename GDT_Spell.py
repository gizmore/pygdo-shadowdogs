from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.spells.Spell import Spell


class GDT_Spell(GDT_Enum):

    SPELLS: dict[str, Spell] = {}

    def gdo_choices(self) -> dict:
        return self.SPELLS
