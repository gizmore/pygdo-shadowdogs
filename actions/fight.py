from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class fight(Action):

    def get_target(self, party: 'GDO_Party'):
        return Shadowdogs.PARTIES.get(party.get_target_string())
