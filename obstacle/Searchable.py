from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Searchable(Obstacle):

    _giving: str

    def __init__(self, name: str = None):
        super().__init__(name)
        self._giving = ''

    def giving(self, item_names: str):
        self._giving = item_names
        return self

    def sd_methods(self) -> list[str]:
        return [
            'sdsearch',
        ]

    async def on_search(self, player: SD_Player):
        if self._giving and not self.gobs('searched'):
            return await self.on_search_success()
        return await super().on_search(player)

    async def on_search_success(self):
        await self.give_new_items(self.get_player(), self._giving, 'search', self.render_name())
        self.sobs('searched', '1')
