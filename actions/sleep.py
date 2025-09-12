from gdo.shadowdogs.actions.Action import Action

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class sleep(Action):

    def get_target(self, party: 'SD_Party', target_string: str):
        from gdo.shadowdogs.engine.World import World
        return World.get_location(target_string)

    async def on_start(self, party: 'SD_Party'):
        pass

    async def sleeping(self, party: 'SD_Party'):
        wakeup = True
        for player in party.members:
            player.give_hp(player.g('p_bod') * Shadowdogs.HP_PER_BODY_SLEEP)
            player.give_mp(player.g('p_mag') * Shadowdogs.MP_PER_MAGIC_SLEEP)
            if (player.g('p_hp') < player.g('p_max_hp')) or (player.g('p_mp') < player.g('p_max_mp')):
                wakeup = False
        if wakeup:
            await party.resume()
            await self.send_to_party(party, 'msg_sd_woke_up')
