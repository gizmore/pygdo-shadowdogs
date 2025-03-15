from gdo.shadowdogs.GDO_Player import GDO_Player


class Loader:

    @classmethod
    def load_cities(cls):
        pass

    @classmethod
    def load_npcs(cls):
        pass

    @classmethod
    def load_parties(cls):
        pass

    @classmethod
    def load_player(cls, player_id: str):
        player = GDO_Player.table().get_by_aid(player_id)
        player.equipment['p_weapon'] = player.gdo_value('p_weapon')