from gdo.base.GDO import GDO
from gdo.base.Trans import t
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Searchable(Obstacle):

    def sd_search_items(self) -> dict[str,int]:
        return GDO.EMPTY_DICT

    def sd_methods(self) -> list[str]:
        return [
            'sdsearch',
        ]

    def on_search(self):
        if items := self.sd_search_items():
            return self.on_search_success()
        return super().on_search()

    def on_search_success(self):
        if not self.gobs('searched'):
            self.give_new_items(self.get_player(), self.sd_search_items(), t('searching'), t(f"obs_{self._name}"))
            self.sobs('searched', '1')
        return super().on_search()

    def giving(self, param):
        pass
