from gdo.shadowdogs.item.classes.Melee import Melee

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Fists(Melee):
    def get_actions(self, player: 'SD_Player') -> list[str]:
        return [
            'sdpunch',
            'sdkick',
        ]
