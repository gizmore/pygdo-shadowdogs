from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.actions.explore import explore
from gdo.shadowdogs.actions.fight import fight
from gdo.shadowdogs.actions.goto import goto
from gdo.shadowdogs.actions.inside import inside
from gdo.shadowdogs.actions.outside import outside
from gdo.shadowdogs.actions.sleep import sleep


class GDT_Action(GDT_Enum):

    def gdo_choices(self) -> dict:
        return {
            'explore': explore(),
            'fight': fight(),
            'goto': goto(),
            'inside': inside(),
            'outside': outside(),
            'sleep': sleep(),
        }
