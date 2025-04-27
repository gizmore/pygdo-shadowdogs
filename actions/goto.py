from gdo.base.Util import Strings
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

from typing import TYPE_CHECKING

from gdo.shadowdogs.locations.Location import Location

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class goto(Action):

    def get_target(self, party: 'SD_Party'):
        ts = party.get_target_string()
        city = getattr(Shadowdogs, Strings.substr_to(ts, '.'))
        return getattr(city, Strings.substr_from(ts, '.'))

    # def get_target_location(self, party: 'SD_Party') -> Location:
    #     return self.get_target(party)
    #
    # def on_start(self, party: 'SD_Party'):
    #     self.send_to_party(party, 'msg_sd_start_goto',
    #                         (self.get_target_location(party).render_name(),
    #                         self.render_busy(party)))