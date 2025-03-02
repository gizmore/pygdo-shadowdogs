from gdo.base.Application import Application
from gdo.base.GDO_Module import GDO_Module
from gdo.shadowdogs.GDO_Inventory import GDO_Inventory
from gdo.shadowdogs.GDO_Item import GDO_Item
from gdo.shadowdogs.GDO_Member import GDO_Member
from gdo.shadowdogs.GDO_NPC import GDO_NPC
from gdo.shadowdogs.GDO_Party import GDO_Party
from gdo.shadowdogs.GDO_Player import GDO_Player


class module_shadowdogs(GDO_Module):

    def gdo_classes(self):
        return [
            GDO_Player,
            GDO_NPC,
            GDO_Party,
            GDO_Member,
            GDO_Item,
            GDO_Inventory,
        ]

    def gdo_subscribe_events(self):
        Application.EVENTS.add_timer(1, self.shadow_timer, 1000000000)

    async def shadow_timer(self):
        pass
