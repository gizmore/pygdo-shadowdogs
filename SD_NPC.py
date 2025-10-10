from typing import Self

from gdo.base.GDT import GDT
from gdo.base.Util import Arrays
from gdo.core.GDO_User import GDO_User

from gdo.shadowdogs.SD_Player import SD_Player


class SD_NPC(SD_Player):

    def is_npc(self) -> bool:
        return True

    def get_user(self) -> GDO_User:
        return GDO_User.system()

    def get_name(self):
        return f"{self.gdo_val('p_npc_name')}[{self.get_id()}]"

    def render_name(self):
        return self.get_name()

    def attack(self, target: SD_Player):
        pass

    @classmethod
    def sd_npc_default_values(cls) -> dict[str, int]:
        return {
        }

    @classmethod
    def blank(cls, vals: dict = None, mark_blank: bool = True) -> Self:
        vals = Arrays.extend_unknown(vals or {}, cls.sd_npc_default_values())
        return super().blank(vals, mark_blank)
