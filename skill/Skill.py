from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Skill(Modifier):

    SKILLS = [
        'p_aim',
        'p_fig',
        'p_hac',
        'p_tra',
        'p_mat',
    ]
