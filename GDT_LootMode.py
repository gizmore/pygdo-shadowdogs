from gdo.base.Trans import t
from gdo.core.GDT_Enum import GDT_Enum


class GDT_LootMode(GDT_Enum):

    KILLER = 'killer'
    CYCLE = 'cycle'
    RANDOM = 'random'

    def gdo_choices(self) -> dict:
        return {
            self.KILLER: t(self.KILLER),
            self.CYCLE: t(self.CYCLE),
            self.RANDOM: t(self.RANDOM),
        }
