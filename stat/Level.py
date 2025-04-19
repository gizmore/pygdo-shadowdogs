from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

class Level(Modifier):

    def apply(self, player: 'SD_Player'):
        player.apply('p_max_hp', self.get_value() * Shadowdogs.HP_PER_LEVEL)
        player.apply('p_max_mp', self.get_value() * Shadowdogs.MP_PER_LEVEL)
