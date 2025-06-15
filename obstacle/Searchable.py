from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Searchable(Obstacle):

    def sd_methods(self) -> list[str]:
        return [
            'sdsearch',
        ]

    def on_search(self):
        pass
