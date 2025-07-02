from gdo.base.GDT import GDT
from gdo.shadowdogs.item.classes.Usable import Usable
from gdo.shadowdogs.obstacle.minigame.Computer import Computer


class Deck(Usable):

    def sd_commands(self) -> list[str]:
        return [
            'sdmove',
        ]

    def get_computer(self) -> Computer:
        return self.get_party().get_target()

    async def on_move(self, direction: str) -> GDT:
        return await self.get_computer().on_move(direction)

