import glob

from gdo.shadowdogs.GDO_Member import GDO_Member
from gdo.shadowdogs.GDO_Party import GDO_Party
from gdo.shadowdogs.GDO_Player import GDO_Player
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class Loader:

    @classmethod
    def module_sd(cls):
        from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
        return module_shadowdogs.instance()

    @classmethod
    def load_cities(cls):
        for path in glob.glob(cls.module_sd().file_path('city/*')):
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
        for slot in GDO_Player.SLOTS:
            player.equipment[slot] = player.gdo_value(slot)
        return player

    @classmethod
    def load_party(cls, party: GDO_Party):
        pids = GDO_Member.table().select('m_player').order('m_created DESC').where(f'm_party={party.get_id()}').exec(False).fetch_column()
        for pid in pids:
            player = cls.load_player(pid)
            Shadowdogs.PLAYERS[player.get_id()] = player
            party.members.append(player)
        Shadowdogs.PARTIES[party.get_id()] = party
