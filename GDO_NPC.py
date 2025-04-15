from gdo.base.GDT import GDT
from gdo.shadowdogs.GDO_Player import GDO_Player


class GDO_NPC(GDO_Player):

    def gdo_table_name(cls) -> str:
        return 'gdo_player'

    def gdo_columns(self) -> list[GDT]:
        cols = super().gdo_columns()
        for col in cols:
            if col.get_name() == 'p_race':
                col.npcs(True)
                break
        return cols

    def is_npc(self) -> bool:
        return True

    def attack(self, target: 'GDO_Player'):
        pass
