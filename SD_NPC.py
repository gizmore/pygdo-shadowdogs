from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User

from gdo.shadowdogs.SD_Player import SD_Player


class SD_NPC(SD_Player):

    def is_npc(self) -> bool:
        return True

    def get_user(self) -> GDO_User:
        return GDO_User.system()

    def get_name(self):
        return self.gdo_val('p_npc_name') + f"[{self.get_id()}]"

    def render_name(self):
        return self.get_name()

    def attack(self, target: SD_Player):
        pass

    def as_real_class(self):
        from gdo.shadowdogs.npcs.npcs import npcs
        npc = npcs.NPCS[self.gdo_val('p_npc_class')]()
        npc._vals = self._vals
        npc._blank = False
        return npc.all_dirty(False)
