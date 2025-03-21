from gdo.base.Application import Application
from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_DateTime import GDT_DateTime
from gdo.date.Time import Time
from gdo.shadowdogs.GDO_Inventory import GDO_Inventory
from gdo.shadowdogs.GDO_Item import GDO_Item
from gdo.shadowdogs.GDO_KnownPlaces import GDO_KnownPlaces
from gdo.shadowdogs.GDO_Member import GDO_Member
from gdo.shadowdogs.GDO_NPC import GDO_NPC
from gdo.shadowdogs.GDO_Party import GDO_Party
from gdo.shadowdogs.GDO_Player import GDO_Player
from gdo.shadowdogs.GDO_Spell import GDO_Spell
from gdo.shadowdogs.engine.Loader import Loader
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
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
            GDO_Spell,
            GDO_KnownPlaces,
        ]

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_UInt('sd_time').not_null().initial('2966371200'),
        ]

    def cfg_time(self) -> int:
        return self.get_config_value('sd_time')

    def gdo_init(self):
        if not Application.IS_HTTP:
            items.load()
            Loader.load_npcs()
            Loader.load_cities()
            Loader.load_parties()

    def gdo_subscribe_events(self):
        Application.EVENTS.add_timer(2, self.shadow_timer, 1000000000)
        Application.EVENTS.add_timer(Shadowdogs.SECONDS_PER_HP, self.shadow_hp_timer, 1000000000)

    async def shadow_timer(self):
        time = self.cfg_time() + Shadowdogs.SECONDS_PER_SECOND
        self.save_config_val('sd_time', str(time))
        for party in Shadowdogs.PARTIES:
            party.tick()
        # dt = self.get_config_value('sd_time')
        # speed = self.get_config_value('sd_speed')
        # dt += speed
        # self.save_config_val('sd_time', Time.get_date(Time.get_time()))
        pass

    async def shadow_hp_timer(self):
        pass