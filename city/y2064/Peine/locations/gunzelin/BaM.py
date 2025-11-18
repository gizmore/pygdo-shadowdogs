from gdo.shadowdogs.SD_Quest import SD_Quest

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class BaM(SD_Quest):

    TIME_SKILL_REQUIRED = 1.0 # time to answer correctly.

    def reward_skills(self, player: 'SD_Player') -> dict[str, int]:
        return {
            'p_mat': 1,
        }
