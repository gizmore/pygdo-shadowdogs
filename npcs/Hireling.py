from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
from gdo.shadowdogs.skill.Trading import Trading


class Hireling(TalkingNPC):

    def sd_can_hire(self) -> bool:
        return True

    def sd_hire_price(self) -> int:
        return 100

    def get_hire_price(self) -> int:
        return Trading.adjust_buy_price(self.get_player(), self.sd_hire_price())

    async def sd_on_hire(self):
        await self.send_to_party(self.get_party(), 'msg_sd_hireling_go')

    async def on_hire(self, player: SD_Player, nuyen: int):
        hireling = Factory.create_hireling(self.__class__)
        await self.get_player().get_party().join(hireling)
        await self.sd_on_hire()

    @classmethod
    def sd_hireling_base(cls) -> dict[str, int|str]:
        return {
            'p_race': 'human',
            'p_gender': 'male',
        }

    @classmethod
    def sd_hireling_bonus(cls) -> dict[str, int | str]:
        return {}

    @classmethod
    def sd_hireling_items(cls) -> list[str]:
        return []
