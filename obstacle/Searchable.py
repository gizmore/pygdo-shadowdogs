from gdo.base.Trans import t
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Searchable(Obstacle):

    _giving: list[str]

    def __init__(self, name: str = None):
        super().__init__(name)
        self._giving = []

    def giving(self, item_name: str):
        self._giving.append(item_name)
        return self

    def sd_methods(self) -> list[str]:
        return [
            'sdsearch',
        ]

    async def on_search(self):
        if self._giving and not self.gobs('searched'):
            return await self.on_search_success()
        return await super().on_search()

    async def on_search_success(self):
        items = []
        for item_name in self._giving:
            items.append(Factory.create_item_gmi(item_name))
        await self.give_items(self.get_player(), items, 'search', t(f"obs_{self._name}"))
        self.sobs('searched', '1')
