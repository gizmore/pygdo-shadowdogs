from gdo.base.Exceptions import GDOException
from gdo.shadowdogs.GDO_Player import GDO_Player
from gdo.shadowdogs.item.Item import Item


class Usable(Item):
    def use(self, player: GDO_Player):
        raise GDOException('err_not_implemented')
