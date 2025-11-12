from gdo.base.Application import Application
from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.Mom import Mom
from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.Thomas import Thomas
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
from gdo.shadowdogs.quest.DeliveryQuest import DeliveryQuest


class Buds(DeliveryQuest):

    ITEM_NAMES = "Weed"
    TARGET_NPC: type[TalkingNPC] = Mom

    def sd_init_quest(self):
        Application.EVENTS.subscribe('sd_on_sleep_over', self.on_slept())

    async def on_slept(self):
        await self.send_to_player(self.get_player(), 'sdqs_mom_needs_weed')
        await self.accept()

    async def on_accomplished(self):
        await self.send_to_player(self.get_player(), 'sdqs_mom_fights_thomas_1')
        await self.send_to_player(self.get_player(), 'sdqs_mom_fights_thomas_2')
        await self.npc_attack(Thomas)
