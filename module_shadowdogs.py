from gdo.base.Application import Application
from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt
from gdo.shadowdogs.SD_Inventory import SD_Inventory
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.SD_Place import SD_Place
from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Spell import SD_Spell
from gdo.shadowdogs.engine.Loader import Loader
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.data.items import items


class module_shadowdogs(GDO_Module):

    def gdo_classes(self):
        return [
            SD_Player,
            SD_NPC,
            SD_Party,
            SD_Item,
            SD_Inventory,
            SD_Spell,
            SD_Place,
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
            Loader.load_parties()

    def gdo_subscribe_events(self):
        Application.EVENTS.add_timer(2, self.shadow_timer, 1000000000)
        Application.EVENTS.add_timer(Shadowdogs.SECONDS_PER_HP_SLEEP, self.shadow_hp_timer, 1000000000)

    async def shadow_timer(self):
        time = self.cfg_time() + Shadowdogs.SECONDS_PER_SECOND
        self.save_config_val('sd_time', str(time))
        for party in Shadowdogs.PARTIES.values():
            party.tick()

    async def shadow_hp_timer(self):
        for party in Shadowdogs.PARTIES.values():
            party.get_action().sleeping(party)

