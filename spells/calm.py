from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.spells.Spell import Spell


class calm(Spell):

    def sd_mana_cost(self, player: SD_Player) -> int:
        return 5

    async def cast(self, player: SD_Player, target: SD_Player|Item):
        pass
