from gdo.base.Util import Strings
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

from typing import TYPE_CHECKING

from gdo.shadowdogs.locations.Location import Location

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class goto(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        ts = target_string
        city = getattr(Shadowdogs, Strings.substr_to(ts, '.'))
        return getattr(city, Strings.substr_from(ts, '.'))
