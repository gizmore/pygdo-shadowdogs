from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class hack(Action):

    def get_target(self, party: 'SD_Party'):
        return party.get_enemy_party()
