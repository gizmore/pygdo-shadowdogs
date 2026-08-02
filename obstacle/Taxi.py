from typing import TYPE_CHECKING

from gdo.base.Exceptions import GDOError
from gdo.base.Trans import t
from gdo.shadowdogs.skill.Trading import Trading

if TYPE_CHECKING:
    from gdo.shadowdogs.locations.Location import Location
    from gdo.shadowdogs.SD_Player import SD_Player

from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class TaxiBase(Obstacle):

    TAXI_COST = 100

    def sd_can_use_on_self(self):
        return True

    def sd_get_taxi_target(self, player: 'SD_Player') -> 'Location':
        raise GDOError('err_not_implemented', ('sd_get_taxi_target',))

    def sd_get_taxi_time(self, player: 'SD_Player') -> int:
        raise GDOError('err_not_implemented', ('sd_get_taxi_time',))

    def sd_get_taxi_price(self, player: 'SD_Player') -> int:
        return Trading.adjust_buy_price(player, self.TAXI_COST)

    def sd_commands(self) -> list[str]:
        return [
            'sduse',
        ]

    async def on_use(self, target: 'SD_Player|Obstacle'):
        player = self.get_player()
        price = self.sd_get_taxi_price(player)
        location = self.sd_get_taxi_target(player)
        if not player.is_leader():
            await self.send_to_player(player, 'err_sd_no_leader')
        elif await player.pay_nuyen(price, t('sd_taxi')):
            await self.send_to_party(self.get_party(), 'msg_sd_taxi_paid', (player.render_name(), ))
            self.get_party()


