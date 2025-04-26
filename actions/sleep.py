from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class sleep(Action):

    def get_target(self, party: 'SD_Party'):
        from gdo.shadowdogs.engine.World import World
        return World.get_location(party.get_target_string())

    async def sleeping(self, party: 'SD_Party'):
        wakeup = True
        for player in party.members:
            player.give_hp(player.g('p_body'))
            player.give_mp(player.g('p_magic'))
            if (player.g('p_hp') < player.g('p_max_hp')) or (player.g('p_mp') < player.g('p_max_mp')):
                wakeup = False
        if wakeup:
            await party.resume()
