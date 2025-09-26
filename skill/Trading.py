from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Trading(Modifier):

    def reduce_buy_price(self, player: 'SD_Player', price: int) -> int:
        return int(round(price * (1.00 - Shadowdogs.STORE_PRICE_REDUCTION_PER_TRADE * player.g('p_tra'))))
