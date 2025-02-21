from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Float import GDT_Float
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.attr.Intelligence import Intelligence
from gdo.shadowdogs.attr.Quickness import Quickness
from gdo.shadowdogs.attr.Strength import Strength


class Player(GDO):

    modified: dict[str, int] = {
        'p_strength': 0.0,
    }

    modified: dict[str, int] = {
        'p_strength': 0.0,
    }

    def __init__(self):
        super().__init__()

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('p_id'),
            GDT_UInt('p_live').bytes(2),
            Strength('p_strength'),
            Quickness('p_quickness'),
            Intelligence('p_intelligence'),
            GDT_Created('p_created'),
            GDT_Creator('p_creator'),
        ]

    def apply(self, name: str, inc: float):
        self._modified[name] += inc

