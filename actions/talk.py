from gdo.base.Render import Mode
from gdo.base.Trans import t
from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party

class talk(Action):

    def render(self, party: 'GDO_Party', mode: Mode) -> str:
        return self.render_party_members(party) + ' ' + t('sd_action_talk', (self.render_target_party(party),))
