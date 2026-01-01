from gdo.base.Util import Random
from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.woods.Fish import Fish
from gdo.shadowdogs.city.y2064.Peine.locations.alfred.quest.Jungle import Jungle
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Woods(Location):

    GIVING: str = 'Bottle'

    NPCS: 'list[type[TalkingNPC]]' = [
        Fish,
    ]

    CHANCE_PERMILLE = 32
    WOLF_PERCENT = 32

    async def on_search(self, player: 'SD_Player'):
        q = Jungle.instance()
        n = int(q.qv_get_inced('jungle_searched'))
        if Random.mrand(0, 1000) < self.CHANCE_PERMILLE and Jungle.instance().is_in_quest():
            await self.send_to_player(player, 'sdqs_found_farm')
            await Jungle.instance().accomplished()
        elif Random.mrand(0, 100) < self.WOLF_PERCENT and Jungle.instance().is_in_quest():
            enemies = await Factory.create_default_npcs(player.get_party().get_location(), "wolf")
            await player.get_party().fight(enemies)
        else:
            await super().on_search(player)

    @classmethod
    def npcs(cls, player: 'SD_Player') -> 'list[type[SD_NPC]]':
        if Jungle.instance().is_in_quest(player):
            return [Fish]
        else:
            return []
