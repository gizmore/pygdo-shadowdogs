from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.city.y2064.Peine.locations.home.quest.Buds import Buds
from gdo.shadowdogs.npcs.TalkingMob import TalkingMob


class Thomas(TalkingMob):

    def sd_quest(self) -> 'type[SD_Quest]|None':
        return Buds

    @classmethod
    def sd_npc_default_values(cls) -> dict[str, int]:
        return {
            'p_str': 2,
        }

    @classmethod
    def sd_npc_default_equipment(cls) -> list[str]:
        return [
            'Jeans',
            'Pullover',
            'Shoes',
        ]

    async def on_say(self, player: SD_Player, text: str):
        if text == 'hello':
            await self.say('sdqs_buds_thomas_hello')
        if self.qv_get('attack'):
            await Buds.instance().on_sd_fight_over(player, player.get_party())
