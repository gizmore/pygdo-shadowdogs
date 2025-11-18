from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Modifier import Modifier
import math
from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class XP(WithShadowFunc, Modifier):

    def __init__(self, name: str):
        super().__init__(name)
        self.bytes(4)
        self.signed(False)
