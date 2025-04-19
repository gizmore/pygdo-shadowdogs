from gdo.core.GDT_User import GDT_User

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class GDT_Player(GDT_User):

    def get_value(self):
        from gdo.shadowdogs.SD_Player import SD_Player
        return SD_Player.table().get_by('p_user', super().get_value().get_id())
