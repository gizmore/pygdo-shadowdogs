import math

from gdo.shadowdogs.GDT_Race import GDT_Race
from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

class Level(Modifier):

    def apply(self, player: 'SD_Player'):
        level = self.get_value()
        player.apply('p_max_hp', int(level * Shadowdogs.HP_PER_LEVEL))
        player.apply('p_max_mp', int(level * Shadowdogs.MP_PER_LEVEL))

    def xp_needed(self, player: 'SD_Player') -> int:
        return math.ceil((self.get_value() + 1) ** GDT_Race.LEVEL_CONSTS[player.gdo_val('p_race')])
