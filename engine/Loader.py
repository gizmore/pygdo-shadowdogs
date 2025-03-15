import glob

from gdo.shadowdogs import module_shadowdogs
from gdo.shadowdogs.GDO_Party import GDO_Party
from gdo.shadowdogs.GDO_Player import GDO_Player


class Loader:

    @classmethod
    def module_sd(cls) -> module_shadowdogs:
        return module_shadowdogs.instance()

    @classmethod
    def load_cities(cls):
        for path in glob.glob(cls.module_sd().file_path('city/')):
            print(path)

    @classmethod
    def load_npcs(cls):
        pass

    @classmethod
    def load_parties(cls):
        parties = GDO_Party.table().select().where("party_action IN ('goto', 'explore', 'sleep')").exec().fetch_all()
        for party in parties:
            cls.load_party(party)

    @classmethod
    def load_player(cls, player_id: str):
        player = GDO_Player.table().get_by_aid(player_id)
        player.equipment['p_weapon'] = player.gdo_value('p_weapon')