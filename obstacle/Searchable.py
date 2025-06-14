from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Searchable(Obstacle):

    def sd_methods(self) -> list[str]:
        return [
            'sdsearh',
        ]

    def on_search(self):
        pass
