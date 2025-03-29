from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party


class sleep(Action):

    def sleeping(self, party: 'GDO_Party'):
        wakeup = True
        for player in party.members:
            player.give_hp(player.g('p_body'))
            player.give_mp(player.g('p_magic'))
            if (player.g('p_hp') < player.g('p_max_hp')) or (player.g('p_mp') < player.g('p_max_mp')):
                wakeup = False
        if wakeup:
            party.resume()
