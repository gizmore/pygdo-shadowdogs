from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Item import GDT_Item
from gdo.shadowdogs.attr.Dexterity import Dexterity
from gdo.shadowdogs.attr.Intelligence import Intelligence
from gdo.shadowdogs.attr.Quickness import Quickness
from gdo.shadowdogs.attr.Strength import Strength
from gdo.shadowdogs.attr.Wisdom import Wisdom
from gdo.shadowdogs.stat.HP import HP
from gdo.shadowdogs.stat.MP import MP


class GDO_Player(GDO):

    modified: dict[str, int]

    def __init__(self):
        super().__init__()
        self.modified = {
            'str': 0,
            'qui': 0,
            'dex': 0,
            'int': 0,
            'wis': 0,

            'hac': 0,
            'fig': 0,

            'hp': 0,
            'mp': 0,

            'mhp': 0,
            'mmp': 0,
        }

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_User('p_id').primary().not_null(),

            GDT_Item('p_weapon'),
            GDT_Item('p_armor'),
            GDT_Item('p_helmet'),
            GDT_Item('p_boots'),
            GDT_Item('p_gloves'),
            GDT_Item('p_amulet'),
            GDT_Item('p_ring'),

            Strength('p_str'),
            Quickness('p_qui'),
            Dexterity('p_dex'),
            Intelligence('p_int'),
            Wisdom('p_wis'),

            HP('p_hp'),
            MP('p_mp'),

            GDT_Created('p_created'),
            GDT_Creator('p_creator'),
        ]

    def kill(self):
        pass

    def apply(self, name: str, inc: int):
        self.modified[name] += inc
        return self

    def modify(self, stats: dict[str, int]):
        for key, val in stats:
            self.apply(key, val)
        return self
