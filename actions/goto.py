from gdo.base.Util import Strings
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party


class goto(Action):

    def get_target(self, party: 'GDO_Party'):
        ts = party.get_target_string()
        city = getattr(Shadowdogs, Strings.substr_to(ts, '.'))
        return getattr(city, Strings.substr_from(ts, '.'))
