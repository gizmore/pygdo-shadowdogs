from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.GDT_Spell import GDT_Spell


class GDO_Spell(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Player('sp_player').primary().cascade_delete(),
            GDT_Spell('sp_spell').primary(),
            GDT_Created('sp_created'),
        ]
