from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.actions.outside import outside
from gdo.shadowdogs.actions.sleep import sleep


class GDT_Action(GDT_Enum):

    def gdo_choices(self) -> dict:
        return {
            'sleep': sleep,
            'outside': outside,
        }
