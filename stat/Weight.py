from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Weight(Modifier):

    def apply(self, player: 'SD_Player'):
        for item in player.all_items():
            player.apply('p_weight', item.get_weight())
        if self.is_overloaded(player):
            player.apply('p_qui', round(-player.modified['p_qui']/2))
            player.apply('p_dex', round(-player.modified['p_dex']/2))

    def max_weight(self, player: 'SD_Player') -> int:
        return player.g('p_str') * Shadowdogs.MAX_WEIGHT_PER_STRENGTH + player.g('p_bod') * Shadowdogs.MAX_WEIGHT_PER_BODY + Shadowdogs.MAX_WEIGHT_BASE

    def is_overloaded(self, player: 'SD_Player'):
        if player.g('p_weight') > int(self.max_weight(player) * Shadowdogs.MAX_WEIGHT_FACTOR):
            return True
        if mount := player.get_mount():
            if not mount.can_move():
                return True
        return False
