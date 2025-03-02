from gdo.core.GDT_User import GDT_User
from gdo.shadowdogs.Player import Player


class GDT_Player(GDT_User):

    def get_player(self) -> Player:
        return Player.get_by_aid(self.get_value().get_id())
