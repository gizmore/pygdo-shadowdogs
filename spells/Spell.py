from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.item.Item import Item


class Spell(WithShadowFunc):

    def sd_mana_cost(self, player: SD_Player) -> int:
        raise ShadowdogsException('err_stub')

    async def cast(self, player: SD_Player, target: SD_Player|Item):
        raise ShadowdogsException('err_stub')
