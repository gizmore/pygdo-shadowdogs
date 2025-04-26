from gdo.core.GDT_Object import GDT_Object

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class GDT_Player(GDT_Object):

    _online: bool
    _nearby: bool
    _humans: bool
    _npcs: bool

    def __init__(self, name: str):
        super().__init__(name)
        from gdo.shadowdogs.SD_Player import SD_Player
        self.table(SD_Player.table())
        self._online = False
        self._nearby = False
        self._humans = True
        self._npcs = False

    def online(self, online: bool=True):
        self._online = online
        return self

    def nearby(self, nearby: bool=True):
        self._nearby = nearby
        return self

    def humans(self, humans: bool=True):
        self._humans = humans
        return self

    def npcs(self, npcs: bool=True):
        self._npcs = npcs
        return self
