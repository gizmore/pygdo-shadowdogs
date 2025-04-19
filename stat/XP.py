from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Modifier import Modifier
import math
from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class XP(WithShadowFunc, Modifier):

    def xp_needed(self, player: 'SD_Player') -> int:
        return math.ceil(player.modified['p_level'] ** Shadowdogs.XP_PER_LEVEL_EXP)

    def apply(self, player: 'SD_Player'):
        if self.get_value() >= self.xp_needed(player):
            self.level_up(player)

    def level_up(self, player: 'SD_Player'):
        player.increment('p_xp', -self.xp_needed(player))
        player.increment('p_level', 1)
        self.send_to_player(player, 'msg_sd_level_up', (player.gdo_val('p_level'), self.xp_needed(player)))
