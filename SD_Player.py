from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from typing import TYPE_CHECKING

from gdo.shadowdogs.SD_Place import SD_Place
from gdo.shadowdogs.GDT_NPCClass import GDT_NPCClass
from gdo.shadowdogs.GDT_RandomName import GDT_RandomName
from gdo.shadowdogs.attr.Magic import Magic
from gdo.shadowdogs.engine.CombatStack import CombatStack
from gdo.shadowdogs.engine.World import World
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.stat.Alcohol import Alcohol
from gdo.shadowdogs.stat.Hunger import Hunger
from gdo.shadowdogs.stat.Karma import Karma
from gdo.shadowdogs.stat.Nuyen import Nuyen
from gdo.shadowdogs.stat.Thirst import Thirst
from gdo.shadowdogs.stat.XP import XP

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.GDT_Faction import GDT_Faction
from gdo.shadowdogs.GDT_Item import GDT_Item
from gdo.shadowdogs.GDT_Party import GDT_Party
from gdo.shadowdogs.GDT_Race import GDT_Race
from gdo.shadowdogs.attr.Body import Body
from gdo.shadowdogs.attr.Charisma import Charisma
from gdo.shadowdogs.attr.Dexterity import Dexterity
from gdo.shadowdogs.attr.Intelligence import Intelligence
from gdo.shadowdogs.attr.Quickness import Quickness
from gdo.shadowdogs.attr.Strength import Strength
from gdo.shadowdogs.attr.Wisdom import Wisdom
from gdo.shadowdogs.engine.Inventory import Inventory
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.item.classes.Fists import Fists
from gdo.shadowdogs.item.classes.Weapon import Weapon
from gdo.shadowdogs.skill.Aim import Aim
from gdo.shadowdogs.skill.Fight import Fight
from gdo.shadowdogs.skill.Hacking import Hacking
from gdo.shadowdogs.stat.HP import HP
from gdo.shadowdogs.stat.Level import Level
from gdo.shadowdogs.stat.MP import MP
from gdo.user.GDT_Gender import GDT_Gender


class SD_Player(GDO):

    SLOTS = [
        'p_weapon',
        'p_armor',
        'p_trousers',
        'p_helmet',
        'p_boots',
        'p_gloves',
        'p_amulet',
        'p_ring',
        'p_piercing',
    ]

    ATTRIBUTES = [
        'p_bod',
        'p_mag',
        'p_str',
        'p_qui',
        'p_dex',
        'p_int',
        'p_wis',
        'p_cha',
    ]

    SKILLS = [
        'p_aim',
        'p_fig',
        'p_hac',
    ]

    party_pos: int
    combat_stack: CombatStack
    modified: dict[str, int]
    equipment: dict[str, 'Item|None']
    inventory: 'Inventory'

    __slots__ = (
        'party_pos',
        'combat_stack',
        'modified',
        'equipment',
        'inventory',
    )

    def __init__(self):
        super().__init__()
        self.modified = {
            'p_bod': 0,
            'p_mag': 0,
            'p_str': 0,
            'p_qui': 0,
            'p_dex': 0,
            'p_int': 0,
            'p_wis': 0,
            'p_cha': 0,

            'p_aim': 0,
            'p_fig': 0,
            'p_hac': 0,

            'p_hp': 0,
            'p_mp': 0,

            'p_max_hp': 0,
            'p_max_mp': 0,

            'p_attack': 0,
            'p_defense': 0,

            'p_marm': 0,
            'p_farm': 0,

            'p_alcohol': 0,
            'p_hunger': 100,
            'p_thirst': 100,

            'p_weight': 0,
            'p_max_weight': 0,
        }
        self.equipment = {}
        for slot in self.SLOTS:
            self.equipment[slot] = None
        self.inventory = Inventory()
        self.party_pos = 0
        self.combat_stack = CombatStack(self)

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('p_id'),

            GDT_User('p_user'),

            GDT_Party('p_party'),
            GDT_UInt('p_joined').bytes(8),

            GDT_NPCClass('p_npc_class'),
            GDT_RandomName('p_npc_name'),

            XP('p_xp'),
            Karma('p_karma'),
            Level('p_level').initial('1'),

            HP('p_hp'),
            MP('p_mp'),

            Nuyen('p_nuyen'),

            GDT_Race('p_race').not_null(),
            GDT_Gender('p_gender').simple().not_null(),
            GDT_Faction('p_faction').initial(GDT_Faction.SEEKER).not_null(),

            GDT_Item('p_weapon'),
            GDT_Item('p_armor'),
            GDT_Item('p_trousers'),
            GDT_Item('p_helmet'),
            GDT_Item('p_boots'),
            GDT_Item('p_gloves'),
            GDT_Item('p_amulet'),
            GDT_Item('p_ring'),
            GDT_Item('p_piercing'),

            Body('p_bod'),
            Magic('p_mag'),
            Strength('p_str'),
            Quickness('p_qui'),
            Dexterity('p_dex'),
            Intelligence('p_int'),
            Wisdom('p_wis'),
            Charisma('p_cha'),

            Aim('p_aim'),
            Fight('p_fig'),
            Hacking('p_hac'),

            Alcohol('p_alcohol'),
            Hunger('p_hunger').initial('50'),
            Thirst('p_thirst').initial('30'),

            GDT_Created('p_created'),
        ]

    def is_npc(self) -> bool:
        return False

    def get_user(self) -> GDO_User:
        return self.gdo_value('p_user')

    def get_name(self):
        if name := self.gdo_val('p_npc_name'):
            return f"{name}[{self.get_id()}]"
        return self.get_user().render_name()

    def new_combat(self, enemies: 'SD_Party'):
        self.combat_stack.reset()
        return self

    def combat_tick(self):
        self.combat_stack.tick()

    def kill(self):
        from gdo.shadowdogs.engine.Factory import Factory
        self.get_party().members.remove(self)
        party = Factory.create_party(World.AmBauhof15.Etage2Left)
        party.members.append(self)
        self.save_val('p_party', party.get_id())
        return self

    def modify_all(self):
        self.column('p_race').apply(self)
        self.column('p_level').apply(self)
        self.column('p_faction').apply(self)
        for key in self.ATTRIBUTES:
            self.column(key).apply(self)
        for key in self.SKILLS:
            self.column(key).apply(self)
        for item in self.inventory:
            item.apply_inv(self)
        for slot in self.SLOTS:
            item = self.gdo_value(slot)
            item.apply_inv(self)
            item.apply(self)
        return self

    def g(self, key: str) -> int:
        return self.modified[key]

    def s(self, key: str, value: int):
        self.modified[key] = value
        return self

    def apply(self, name: str, inc: int):
        self.modified[name] += inc
        return self

    def modify(self, stats: dict[str, int]):
        for key, val in stats.items():
            self.apply(key, val)
        return self

    def get_weapon(self) -> 'Weapon':
        return self.equipment['p_weapon'] or Fists()

    def give_hp(self, hp: int):
        return self.s('p_hp', min(self.g('p_hp') + hp, self.g('p_max_hp')))

    def give_mp(self, mp: int):
        return self.s('p_mp', min(self.g('p_mp') + mp, self.g('p_max_mp')))

    def get_party(self) -> 'SD_Party':
        return self.gdo_value('p_party')

    def has_kp(self, location: 'Location') -> bool:
        return SD_Place.has_location(self, location)

    def hit(self, dmg: int):
        self.give_hp(-dmg)
        if self.g('p_hp') <= 0:
            self.kill()

    def render_ny(self):
        return
        pass
