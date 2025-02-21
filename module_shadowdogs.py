from gdo.base.GDO_Module import GDO_Module
from gdo.shadowdogs.Player import Player


class module_shadowdogs(GDO_Module):

    def gdo_classes(self):
        return [
            Player,
        ]
