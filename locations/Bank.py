from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Location import Location
from gdo.ui.GDT_Error import GDT_Error
from gdo.ui.GDT_Success import GDT_Success


class Bank(Location):

    async def on_push(self, player: SD_Player, item: Item, amount: int = 1):
        player.bank.add_item(item)
        item2 = player.inventory.remove_item(item.render_name_wc(), amount)
        if item2 is None:
            return GDT_Error().text('err_sd_item_amount', (item.render_name_wc(), amount, item.get_count()))
        item2.save_val('item_slot', GDT_Slot.BANK)
        return GDT_Success().text('msg_sd_bank_pushed', (amount, item.render_name_wc()))

    async def on_pop(self, player: SD_Player) -> None:
        pass

    