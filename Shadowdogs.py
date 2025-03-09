from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player


class Shadowdogs:

    MAX_WEIGHT_PER_STRENGTH = 1000

    @classmethod
    def send_to_player(cls, player: 'GDO_Player', text: str):
        player.get_user()