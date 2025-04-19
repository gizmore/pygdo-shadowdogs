from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class fight(Action):

    def get_target(self, party: 'SD_Party'):
        return Shadowdogs.PARTIES.get(party.get_target_string())

    def execute(self, party: 'SD_Party'):
        for player in party.members:
            player.combat_tick()
