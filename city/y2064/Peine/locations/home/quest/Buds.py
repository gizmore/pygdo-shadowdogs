from functools import partial

from gdo.base.Application import Application
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.Mom import Mom
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
        from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.Thomas import Thomas
        await self.send_to_player(self.get_player(), 'sdqs_mom_fights_thomas_1')
        await self.send_to_player(self.get_player(), 'sdqs_mom_fights_thomas_2')
        await self.npc_attack(Thomas)
        self.qv_set('attack', '1')
        Application.EVENTS.subscribe_once('on_sd_fight_over', partial(self.on_sd_fight_over, self.get_player()))

    async def on_sd_fight_over(self, player: SD_Player, party: SD_Player):
        self.qv_set('attack', '')
        await self.send_to_player(player, 'sdqs_thomas_dart')
        await self.give_spell(player, 'dart', 'sd_fighting_thomas')
