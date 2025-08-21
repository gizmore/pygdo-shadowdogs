from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Lazer(TalkingNPC):

    async def on_say(self, player: SD_Player, text: str):
        if self.qv_get('lazer2'):
            await self.send_to_player(player, 'sd_lazer_home_intro3')
            self.qv_set('lazer3')
        elif self.qv_get('lazer1'):
            await self.send_to_player(player, 'sd_lazer_home_intro2')
            self.qv_set('lazer2')
        else:
            await self.send_to_player(player, 'sd_lazer_home_intro1')
            self.qv_set('lazer1')
        await self.give_word(player, 'hello')
