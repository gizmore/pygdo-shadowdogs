import functools

from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.Inventory import Inventory
from gdo.shadowdogs.engine.ItemList import ItemList
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.item.data.items import items
from gdo.shadowdogs.locations.Location import Location


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
            item_list.append(items.get_item(item_name).buy_price(price).shop_position(i))
            i += 1
        return item_list

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
