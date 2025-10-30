from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Trading(Modifier):

    @classmethod
    def adjust_buy_price(cls, player: 'SD_Player', price: int) -> int:
        return int(round(price * (1.00 - Shadowdogs.STORE_PRICE_REDUCTION_PER_TRADE * player.g('p_tra') - Shadowdogs.STORE_PRICE_REDUCTION_PER_CHARISMA * player.g('p_cha'))))

    @classmethod
    def adjust_sell_price(cls, player: 'SD_Player', price: int) -> int:
        return (price + cls.adjust_buy_price(player, price)) // 2
