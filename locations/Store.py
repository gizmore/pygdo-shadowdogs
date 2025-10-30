import functools

from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.Inventory import Inventory
from gdo.shadowdogs.engine.ItemList import ItemList
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.item.data.items import items
from gdo.shadowdogs.locations.Location import Location
from gdo.ui.GDT_Error import GDT_Error
from gdo.ui.GDT_Success import GDT_Success


class Store(Location):

    ITEMS: list[tuple[str,int]] = [
    ]

    def sd_get_shop_items(self, player: SD_Player):
        return self.ITEMS

    def sd_allow_sell(self) -> bool:
        return False

    def sd_allow_buy(self) -> bool:
        return True

    def get_shop_items(self, player: SD_Player):
        item_list = ItemList()
        i = 1
        for item_name, price in self.sd_get_shop_items(player):
            item_list.append(items.get_item(item_name).buy_price(self.get_buy_price(player, price)).shop_position(i))
            i += 1
        return item_list

    def get_buy_price(self, player: SD_Player, price: int) -> int:
        return player.c('p_tra').adjust_buy_price(player, price)

    @functools.lru_cache(maxsize=None)
    def sd_methods(self) -> list[str]:
        methods = []
        if self.sd_allow_buy():
            methods.append('sdbuy')
            methods.append('sdview')
            methods.append('sdviewitem')
        if self.sd_allow_sell():
            methods.append('sdsell')
        return methods

    async def on_buy(self, player: SD_Player, item: Item, amt: int = 1):
        have_ny = player.get_nuyen()
        need_ny = item._buy_price * amt
        if need_ny > have_ny:
            return GDT_Error().text('err_sd_money_to_buy', (item.render_name(), Shadowdogs.display_nuyen(need_ny), Shadowdogs.display_nuyen(have_ny)))
        await self.give_item(player, item.set_value('item_count', amt))
        player.give_nuyen(-need_ny)
        return GDT_Success().text('msg_sd_bought', (item.render_name(), Shadowdogs.display_nuyen(need_ny), Shadowdogs.display_nuyen(have_ny - need_ny)))
