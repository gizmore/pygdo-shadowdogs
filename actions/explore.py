from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party


class explore(Action):

    def get_target(self, party: 'GDO_Party'):
        return getattr(Shadowdogs, party.get_target_string())
