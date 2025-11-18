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
    def get_for_player(cls, player: 'SD_Player', spell: 'Spell') -> 'SD_Spell|None':
        return cls.table().select().where(f"sp_player={player.get_id()} AND sp_spell='{spell.get_name()}'").first().exec().fetch_object()

    @classmethod
    def create_for_player(cls, player: 'SD_Player', spell: 'Spell') -> 'SD_Spell|None':
        return cls.blank({
            'sp_spell': spell.get_name(),
            'sp_player': player.get_id(),
        }).soft_replace()

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Spell('sp_spell').primary(),
            GDT_Player('sp_player').primary().cascade_delete(),
            GDT_UInt('sp_casted').not_null().initial('0'),
            GDT_Created('sp_created'),
        ]

    def get_spell(self) -> 'Spell':
        return self.gdo_value('sp_spell')
