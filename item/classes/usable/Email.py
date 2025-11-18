from gdo.shadowdogs.item.classes.Usable import Usable

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Email(Usable):

    def get_key(self) -> str:
        return self.dm('key')

    def get_args(self) -> tuple:
        return ()

    def sd_can_use_on_self(self) -> bool:
        return True

    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        await self.send_to_player(self.get_player(), self.get_key(), self.get_args())
