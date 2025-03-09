from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Faction import GDT_Faction
from gdo.shadowdogs.GDT_Item import GDT_Item
from gdo.shadowdogs.GDT_Party import GDT_Party
from gdo.shadowdogs.GDT_Race import GDT_Race
from gdo.shadowdogs.attr.Body import Body
from gdo.shadowdogs.attr.Dexterity import Dexterity
from gdo.shadowdogs.attr.Intelligence import Intelligence
from gdo.shadowdogs.attr.Quickness import Quickness
from gdo.shadowdogs.attr.Strength import Strength
from gdo.shadowdogs.attr.Wisdom import Wisdom
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.item.classes.Weapon import Weapon
from gdo.shadowdogs.skill.Fight import Fight
from gdo.shadowdogs.skill.Hacking import Hacking
from gdo.shadowdogs.stat.HP import HP
from gdo.shadowdogs.stat.MP import MP
from gdo.user.GDT_Gender import GDT_Gender


class GDO_Player(GDO):

    modified: dict[str, int]
    equipment: dict[str, 'Item']

    def __init__(self):
        super().__init__()
        self.modified = {
            'p_bod': 0,
            'p_str': 0,
            'p_qui': 0,
            'p_dex': 0,
            'p_int': 0,
            'p_wis': 0,

            'p_hac': 0,
            'p_fig': 0,

            'p_hp': 0,
            'p_mp': 0,

            'max_hp': 0,
            'max_mp': 0,

            'atk': 0,
            'def': 0,

            'weight': 0,
            'max_weight': 0,
        }

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_User('p_id').primary().not_null(),
            GDT_Party('p_party'),

            HP('p_hp'),
            MP('p_mp'),

            GDT_Race('p_race').not_null(),
            GDT_Gender('p_gender').simple().not_null(),
            GDT_Faction('p_faction').initial(GDT_Faction.SEEKER).not_null(),

            GDT_Item('p_weapon').initial('Fists'),
            GDT_Item('p_armor'),
            GDT_Item('p_helmet'),
            GDT_Item('p_boots'),
            GDT_Item('p_gloves'),
            GDT_Item('p_amulet'),
            GDT_Item('p_ring'),

            Body('p_bod'),
            Strength('p_str'),
            Quickness('p_qui'),
            Dexterity('p_dex'),
            Intelligence('p_int'),
            Wisdom('p_wis'),

            Fight('p_fig'),
            Hacking('p_hac'),

            GDT_Created('p_created'),
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

    def get_weapon(self) -> 'Weapon':
        pass
