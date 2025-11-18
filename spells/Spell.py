from gdo.base.Trans import t
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.item.Item import Item


class Spell(WithShadowFunc):

    def __init__(self) -> None:
        super().__init__()
        self._level = 1

    def get_name(self) -> str:
        return self.__class__.__name__

    def level(self, level: int):
        self._level = level
        return self

    def get_level(self) -> int:
        return self._level

    def sd_mana_cost(self, player: SD_Player) -> int:
        raise ShadowdogsException('err_stub', (f"{self.get_name()}.sd_mana_cost()", ))

    def sd_cast_time(self, player: SD_Player) -> int:
        return 60

    async def precast(self, player: SD_Player, target: SD_Player|Item):
        raise ShadowdogsException('err_stub', (f"{self.get_name()}.precast()", ))

    async def cast(self, player: SD_Player, target: SD_Player|Item):
        raise ShadowdogsException('err_stub', (f"{self.get_name()}.cast()", ))

    def render_name(self):
        return t("sd_spell_"+self.get_name())   
