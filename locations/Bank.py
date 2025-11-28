import re

from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.locations.Location import Location
from gdo.ui.GDT_Error import GDT_Error
from gdo.ui.GDT_Success import GDT_Success


class Bank(Location):

    def sd_methods(self) -> list[str]:
        return [
            'sdpush',
            'sdpop',
            'sdview',
            'sdviewitem',
        ]

    def get_shop_items(self, player: SD_Player):
        return player.get_bank_items()

    async def on_push(self, player: SD_Player, item: Item):
        item2 = player.inventory.remove_item(item.render_name())
        if item2 is None:
            return GDT_Error().text('err_sd_item_amount', (item.render_name(),))
        item2.save_val('item_slot', GDT_Slot.BANK)
        player.get_bank_items().add_item(item)
        return GDT_Success().text('msg_sd_bank_pushed', (item.render_name(),))

    async def on_pop(self, player: SD_Player, item: Item) -> None:
        item2 = player.get_bank_items().remove_item(item.render_name())
        item2.save_val('item_slot', GDT_Slot.INVENTORY)
        player.inventory.add_item(item)
        return GDT_Success().text('msg_sd_bank_poppped', (item.render_name(),))

    