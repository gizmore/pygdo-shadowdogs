import math

from gdo.base.Application import Application
from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDT import GDT
from gdo.base.Message import Message
from gdo.core.GDT_Char import GDT_Char
from gdo.core.GDT_UInt import GDT_UInt
from gdo.shadowdogs.InstallShadowdogs import InstallShadowdogs
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.SD_KnownWord import SD_KnownWord
from gdo.shadowdogs.SD_Location import SD_Location
from gdo.shadowdogs.SD_ObstacleVal import SD_ObstacleVal
from gdo.shadowdogs.SD_Place import SD_Place
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.SD_QuestDone import SD_QuestDone
from gdo.shadowdogs.SD_QuestVal import SD_QuestVal
from gdo.shadowdogs.SD_Spell import SD_Spell
from gdo.shadowdogs.SD_Word import SD_Word
from gdo.shadowdogs.engine.Loader import Loader
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.data.items import items


class module_shadowdogs(GDO_Module):

    def __init__(self):
        super().__init__()

    def gdo_classes(self):
        return [
            SD_Location,
            SD_Player,
            SD_Party,
            SD_Item,
            SD_Spell,
            SD_Place,
            SD_Quest,
            SD_QuestDone,
            SD_QuestVal,
            SD_ObstacleVal,
            SD_Word,
            SD_KnownWord,
        ]

    def gdo_install(self):
        Loader.init_npc_classes()
        InstallShadowdogs.install()

    def gdo_init(self):
        Loader.init_npc_classes()
        if not Application.IS_HTTP and self.is_persisted():
            items.load()
            Loader.cleanup()
            Loader.load_npcs()
            Loader.load_parties()

    ##########
    # Config #
    ##########

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_UInt('sd_time').not_null().initial('2966371200'),
        ]

    def cfg_time(self) -> int:
        return math.floor(Application.TIME)

    def gdo_user_settings(self) -> list[GDT]:
        return [
            GDT_UInt('sd_distance').not_null().min(2).max(Shadowdogs.MAX_DISTANCE).initial('2'),
            GDT_Char('sd_shortcut').not_null().initial('#').maxlen(1).minlen(1).not_null().initial('#'),
        ]

    def cfg_shortcut(self) -> str:
        return self.get_config_val('sd_shortcut')

    ##########
    # Events #
    ##########

    def gdo_subscribe_events(self):
        Application.EVENTS.add_timer(Shadowdogs.SECONDS_PER_TICK, self.shadow_timer, 1000000000)
        Application.EVENTS.add_timer(Shadowdogs.SECONDS_PER_HP_SLEEP, self.shadow_hp_timer, 1000000000)
        Application.EVENTS.add_timer(Shadowdogs.SECONDS_PER_FOODING, self.shadow_food_timer, 1000000000)
        Application.EVENTS.subscribe('new_message', self.sd_alias)

    async def shadow_timer(self):
        for party in list(Shadowdogs.PARTIES.values()):
            await party.tick()

    async def shadow_hp_timer(self):
        for party in Shadowdogs.PARTIES.values():
            await party.get_action().sleeping(party)

    async def shadow_food_timer(self):
        for party in Shadowdogs.PARTIES.values():
            await party.digesting()

    async def sd_alias(self, message: Message):
        trig = message._env_user.get_setting_val('sd_shortcut')
        if message._message.startswith(f"{trig}"):
            message._message = message.get_trigger() + "sd" + message._message[1:]
