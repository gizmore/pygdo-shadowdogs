from gdo.core.GDT_User import GDT_User

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player


class GDT_Player(GDT_User):

    def get_player(self) -> 'GDO_Player':
        from gdo.shadowdogs.GDO_Player import GDO_Player
        return GDO_Player.table().get_by_aid(self.get_value().get_id())
