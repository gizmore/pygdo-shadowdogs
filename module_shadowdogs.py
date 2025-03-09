from gdo.base.Application import Application
from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_DateTime import GDT_DateTime
from gdo.date.Time import Time
from gdo.shadowdogs.GDO_Inventory import GDO_Inventory
from gdo.shadowdogs.GDO_Item import GDO_Item
from gdo.shadowdogs.GDO_Member import GDO_Member
from gdo.shadowdogs.GDO_NPC import GDO_NPC
from gdo.shadowdogs.GDO_Party import GDO_Party
from gdo.shadowdogs.GDO_Player import GDO_Player
from gdo.shadowdogs.engine.Loader import Loader
from gdo.shadowdogs.item.data.items import items


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

    def gdo_module_config(self) -> list[GDT]:
        return [
            # GDT_UInt('sd_speed').initial('12').not_null(),
            # GDT_DateTime('sd_time').initial('2064-12-24').not_null(),
        ]

    def gdo_init(self):
        if not Application.IS_HTTP:
            items.load()
            Loader.load_npcs()
            Loader.load_cities()

    def gdo_subscribe_events(self):
        Application.EVENTS.add_timer(1, self.shadow_timer, 1000000000)

    async def shadow_timer(self):
        # dt = self.get_config_value('sd_time')
        # speed = self.get_config_value('sd_speed')
        # dt += speed
        # self.save_config_val('sd_time', Time.get_date(Time.get_time()))
        pass
