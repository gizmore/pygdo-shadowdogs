from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_UInt import GDT_UInt
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.GDT_Spell import GDT_Spell
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.spells.Spell import Spell


class SD_Spell(GDO):

    @classmethod
    def get_for_player(cls, player: 'SD_Player', name: str) -> 'SD_Spell|None':
        return cls.table().get_by_id(name, player.get_id())

    @classmethod
    def create_for_player(cls, player: 'SD_Player', spell: str, level: int = 1) -> 'SD_Spell|None':
        return cls.blank({
            'sp_spell': spell,
            'sp_player': player.get_id(),
            'sp_level': str(level),
        }).soft_replace()

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Spell('sp_spell').primary(),
            GDT_Player('sp_player').primary().cascade_delete(),
            GDT_UInt('sp_level').bytes(1).not_null().initial('1'),
            GDT_UInt('sp_casted').not_null().initial('0'),
            GDT_UInt('sp_failed').not_null().initial('0'),
            GDT_Created('sp_learned'),
        ]

    def get_spell(self) -> 'Spell':
        return self.gdo_value('sp_spell')

    def get_level(self) -> int:
        return self.gdo_value('sp_level')
