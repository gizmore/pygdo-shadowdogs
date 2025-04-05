from gdo.base.Method import Method
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.method.buy import buy
from gdo.shadowdogs.method.sell import sell
from gdo.shadowdogs.method.view import view


class Store(Location):

    def sd_allow_sell(self) -> bool:
        return True

    def sd_methods(self) -> list[Method]:
        methods = [
            view(),
            buy(),
        ]
        if self.sd_allow_sell():
            methods.append(sell())
        return methods

