from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.item.classes.Usable import Usable


class Mail(Usable):

    def sd_inv_type(self) -> str:
        return GDT_Slot.CYBERDECK

    def sd_commands(self) -> list[str]:
        return [
            'sdread',
        ]

    async def on_use(self):
        await self.send_to_player(self.get_player(), self.dm('key'), None)

