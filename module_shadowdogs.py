from gdo.base.Application import Application
from gdo.base.GDO_Module import GDO_Module
from gdo.base.Logger import Logger
from gdo.shadowdogs.Member import Member
from gdo.shadowdogs.Party import Party
from gdo.shadowdogs.Player import Player


class module_shadowdogs(GDO_Module):

    def gdo_classes(self):
        return [
            Party,
            Player,
            Member,
        ]

    def gdo_subscribe_events(self):
        Application.EVENTS.add_timer(1, self.shadow_timer, 1000000000)

    async def shadow_timer(self):
        Logger.debug("shadow_timer")
