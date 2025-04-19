from gdo.base.Exceptions import GDOException
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.item.Item import Item


class Usable(Item):
    def use(self, player: SD_Player):
        raise GDOException('err_not_implemented')
