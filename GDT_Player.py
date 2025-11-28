from gdo.base.GDO import GDO
from gdo.core.GDT_Object import GDT_Object

from typing import TYPE_CHECKING

from gdo.core.GDT_User import GDT_User
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class GDT_Player(WithShadowFunc, GDT_Object):
    """
    TODO annotate SD_Player, GDT_User
    TODO describe options members, online, nearby, humans by username, npcs (by id)
    """

    _members: bool
    _online: bool
    _nearby: bool
    _humans: bool
    _npcs: bool
    _gdt_user: GDT_User

    def __init__(self, name: str):
        super().__init__(name)
        from gdo.shadowdogs.SD_Player import SD_Player
        self.table(SD_Player.table())
        self._members = False
        self._online = False
        self._nearby = False
        self._humans = True
        self._npcs = False
        self._gdt_user = GDT_User(name+"_user")

    def online(self, online: bool=True):
        self._online = online
        return self

    def members(self, members: bool=True):
        self._members = members
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

    def query_gdos(self, val: str) -> list[GDO]:
        val = val.lower()
        players = self.query_gdos2(val)
        if self._nearby:
            near = []
            for player in players:
                if player.is_near(self.get_player()):
                    near.append(player)
            players = near
        if self._online:
            on = []
            for player in players:
                if player.get_id() in Shadowdogs.PLAYERS:
                    on.append(player)
            players = on
        if not val.isdigit():
            keep = []
            for player in players:
                if player.render_name().lower().startswith(val):
                    keep.append(player)
            if len(keep) == 1:
                return keep
            keep = []
            for player in players:
                if val in player.render_name().lower():
                    keep.append(player)
            players = keep
        return players

    def query_gdos2(self, val: str) -> list['SD_Player']:
        if self._members:
            if val.isdigit():
                return [self.get_party().members[int(val)-1]]
        if self._npcs and val.isdigit():
            if player := self._table.get_by_aid(val):
                return [player]
        if self._npcs:
            return [p.player(Shadowdogs.CURRENT_PLAYER) for p in self.get_location().NPC_INSTANCES]
        if self._humans:
            query = self._table.select().join_object('p_user')
            return self._gdt_user.val(val).query_gdos_query(val, query).exec().fetch_all()._items
        return GDO.EMPTY_LIST
