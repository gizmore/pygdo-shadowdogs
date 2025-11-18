from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.market.Etablisment import Etablisment
from gdo.shadowdogs.npcs.Hireling import Hireling


class Lazer(Hireling):

    def sd_quest(self) -> type[SD_Quest]|None:
        return Etablisment

    async def on_say(self, player: SD_Player, text: str):
        if self.qv_get('lazer3'):
            await self.give_word(player, 'home')
        elif self.qv_get('lazer2'):
            await self.send_to_player(player, 'sd_lazer_home_intro3')
            self.qv_set('lazer3')
            await self.give_word(player, 'weed')
        elif self.qv_get('lazer1'):
            await self.send_to_player(player, 'sd_lazer_home_intro2')
            self.qv_set('lazer2')
        else:
            await self.send_to_player(player, 'sd_lazer_home_intro1')
            self.qv_set('lazer1')
        await self.give_word(player, 'hello')

    @classmethod
    def sd_npc_default_equipment(cls) -> list[str]:
        return [
            'Jeans',
            'Pullover',
            'Shoes',
            'Kadett',
        ]

    @classmethod
    def sd_npc_default_values(cls):
        return {
            'p_bod': 4,
            'p_str': 4,
            'p_qui': 2,
        }
