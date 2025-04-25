from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.SD_Player import SD_Player


class SD_NPC(SD_Player):

    def gdo_columns(self) -> list[GDT]:
        cols = super().gdo_columns()
        for col in cols:
            if col.get_name() == 'p_race':
                col.npcs(True)
                break
        return cols

    def is_npc(self) -> bool:
        return True

    def get_user(self) -> GDO_User:
        return GDO_User.system()

    def attack(self, target: 'SD_Player'):
        pass
