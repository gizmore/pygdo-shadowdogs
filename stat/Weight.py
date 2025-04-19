from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.Modifier import Modifier


class Weight(Modifier):

    def apply(self, player: 'SD_Player'):
        for item in player.all_items():
            player.apply('p_weight', item.get_weight())
        if player.is_overloaded():
            player.apply('p_qui', round(-player.modified['p_qui']/2))
            player.apply('p_str', round(-player.modified['p_str']/2))
            player.apply('p_dex', round(-player.modified['p_dex']/2))
