from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Skill(Modifier):

    SKILLS = [
        'p_tra',
        'p_aim',
        'p_fig',
        'p_hac',
        'p_cry',
        'p_mat',
    ]

    def __init__(self, name: str):
        super().__init__(name)
        self.initial('-1')
