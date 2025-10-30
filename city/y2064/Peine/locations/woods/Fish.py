from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.alfred.quest.Jungle import Jungle
from gdo.shadowdogs.npcs.Hireling import Hireling
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Fish(Hireling):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Jungle

    @classmethod
    def sd_npc_default_values(cls) -> dict[str, int]:
        return {
            'p_max_ho': 5,
            'p_race': 'human',
            'p_gender': 'male',
        }

    async def on_say(self, player: SD_Player, text: str):
        q = self.q()
        n = q.qv_get_inced('say', player, 3)
        await self.say(f'sdqs_jungle_keep_on_{n}')
