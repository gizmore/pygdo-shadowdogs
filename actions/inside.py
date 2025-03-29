from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party

class inside(Action):

    def get_target(self, party: 'GDO_Party'):
        from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
        return Shadowdogs.get_location(party.get_target_string())
