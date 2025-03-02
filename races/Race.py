from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.engine.Modifier import Modifier


class Race(Modifier, GDT_Enum):
    BONUS = {
        'elve': {'str': 0},
        'human': {'str': 0},
        'ork': {'str': 0},
        'dragon': {'str': 0},
        'animal': {'str': 0},
    }

    def __init__(self, name: str):
        super().__init__(name)


