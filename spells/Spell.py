from gdo.base.Trans import t
from gdo.base.Util import Random
from gdo.date.Time import Time
from gdo.message.GDT_HTML import GDT_HTML
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


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

    def sd_works_on_friends(self) -> bool:
        return True

    def sd_works_on_foes(self) -> bool:
        return True

    def sd_works_on_obstacles(self) -> bool:
        return False

    def sd_works_on_items(self) -> bool:
        return False

    def sd_mp_cost(self, player: SD_Player) -> int:
        raise ShadowdogsException('err_stub', (f"{self.get_name()}.sd_mana_cost()", ))

    def sd_cast_time(self, player: SD_Player) -> int:
        raise ShadowdogsException('err_stub', (f"{self.get_name()}.sd_cast_time()", ))

    async def precast(self, player: SD_Player, target: SD_Player|Item):
        raise ShadowdogsException('err_stub', (f"{self.get_name()}.precast()", ))

    async def sd_cast(self, player: SD_Player, target: SD_Player | Item):
        raise ShadowdogsException('err_stub', (f"{self.get_name()}.on_cast()", ))

    async def cast(self, player: SD_Player, target: SD_Player|Item|None):
        target = target or player
        if target.is_friend() and not self.sd_works_on_friends():
            return self.send_to_player(player, 'err_sd_spell_not_on_friends')
        if target.is_foe() and not self.sd_works_on_foes():
            return self.send_to_player(player, 'err_sd_spell_not_on_foes')
        if isinstance(target, Obstacle) and not self.sd_works_on_obstacles():
            return self.send_to_player(player, 'err_sd_spell_not_on_obstacles')
        if isinstance(target, Item) and not self.sd_works_on_items():
            return self.send_to_player(player, 'err_sd_spell_not_on_items')
        if not await self.cast_fail(player, target):
            player.give_mp(-self.sd_mp_cost(player))
            await self.sd_cast(player, target)
        return GDT_HTML()

    def render_name(self):
        return t("sd_spell_"+self.get_name())

    async def cast_fail(self, player: SD_Player, target: SD_Player|Item|None):
        if Random.mrand(0, round(self.get_level() * Shadowdogs.CAST_FAIL_MULTIPLE_PER_LEVEL)) > player.g('p_wis'):
            cost = round(self.sd_mp_cost(player) / 2)
            player.give_mp(-cost)
            await self.send_to_party(self.get_party(), 'msg_sd_cast_fail', (self.get_name(), cost, player.gb('p_mp')))
            return True
        return False

    def get_cast_text_p(self, player: SD_Player, target: SD_Player|Item|None):
        return self.t('msg_sd_cast_p', (player.render_name(), self.sd_mp_cost(player), player.gb('p_mp'), self.get_level(), self.get_name(), target.render_name(), player.render_busy()))

    def get_cast_text_e(self, player: SD_Player, target: SD_Player | Item | None):
        return self.t('msg_sd_cast_e', (player.render_name(), self.sd_mp_cost(player), self.get_name(), target.render_name(), player.render_busy()))
