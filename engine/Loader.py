from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class Loader(WithShadowFunc):

    @classmethod
    def load_npcs(cls):
        pass

    @classmethod
    def load_parties(cls):
        parties = (SD_Party.table().select().
                   where("party_action IN ('goto', 'explore', 'talk', 'sleep', 'travel', 'fight', 'hack')").
                   exec().fetch_all())
        for party in parties:
            cls.load_party(party)

    @classmethod
    def load_party(cls, party: SD_Party):
        pids = SD_Player.table().select().order('p_created DESC').where(f'p_party={party.get_id()}').exec(False).fetch_column()
        for pid in pids:
            if pid not in Shadowdogs.PLAYERS:
                player = SD_Player.table().get_by_aid(pid).as_real_class()
                Shadowdogs.PLAYERS[player.get_id()] = player
                Shadowdogs.USERMAP[player.gdo_val('p_user')] = player
                party.members.append(player)

        Shadowdogs.PARTIES[party.get_id()] = party
        return party

    @classmethod
    def load_user(cls, user: GDO_User) -> SD_Player | None:
        if party_id := SD_Player.table().select('p_party').where(f'p_user={user.get_id()}').first().exec().fetch_val():
            if party_id not in Shadowdogs.PARTIES:
                cls.load_party(SD_Party.table().get_by_aid(party_id))
            return Shadowdogs.USERMAP[user.get_id()]
        return None

    # @classmethod
    # def load_player(cls, player_id: str):
    #     player = SD_Player.table().get_by_aid(player_id)
    #     for slot in SD_Player.SLOTS:
    #         player.equipment[slot] = player.gdo_value(slot)
    #     return player

