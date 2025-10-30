from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
from gdo.shadowdogs.skill.Trading import Trading


class Hireling(TalkingNPC):

    def sd_can_hire(self) -> bool:
        return True

    def sd_hire_price(self) -> int:
        return 100

    def get_hire_price(self) -> int:
        return Trading.adjust_buy_price(self.get_player())

    async def sd_on_hire(self):
        await self.send_to_party(self.get_party(), 'msg_sd_hireling_go')

    async def on_hire(self):
        hireling = Factory.create_hireling(self.__class__)
        await self.get_player().get_party().join(hireling)
        await self.sd_on_hire()
