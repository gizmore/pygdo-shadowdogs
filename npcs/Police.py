from typing import Self

from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class Police(SD_NPC):

    @classmethod
    def blank(cls, vals: dict = None, mark_blank: bool = True) -> Self:
        police = super().blank(vals, mark_blank)
        player = Shadowdogs.CURRENT_PLAYER
        police.sb('p_level', player.get_party().gmax('p_level'))
        return police

    def ai_decision(self) -> str:
        return 'sdp'
