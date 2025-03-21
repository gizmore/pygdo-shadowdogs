from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.spells.Spell import Spell
from gdo.shadowdogs.spells.calm import calm


class GDT_Spell(GDT_Enum):

    SPELLS: dict[str, Spell] = {
        'calm': calm(),
    }

    def gdo_choices(self) -> dict:
        return self.SPELLS
