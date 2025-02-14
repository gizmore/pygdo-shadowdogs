from gdo.base.GDO_Module import GDO_Module
from gdo.shadowdogs.Player import GDO_Player


class module_shadowdogs(GDO_Module):

    def gdo_classes(self):
        return [
            GDO_Player,
        ]
