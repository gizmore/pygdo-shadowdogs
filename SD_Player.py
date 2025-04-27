from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from typing import TYPE_CHECKING

from gdo.date.Time import Time
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.SD_Place import SD_Place
from gdo.shadowdogs.GDT_NPCClass import GDT_NPCClass
from gdo.shadowdogs.GDT_RandomName import GDT_RandomName
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.attr.Magic import Magic
from gdo.shadowdogs.engine.CombatStack import CombatStack
from gdo.shadowdogs.engine.Modifier import Modifier
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.classes.Equipment import Equipment
from gdo.shadowdogs.skill.Skill import Skill
from gdo.shadowdogs.skill.Trading import Trading
from gdo.shadowdogs.stat.Alcohol import Alcohol
from gdo.shadowdogs.stat.Hunger import Hunger
from gdo.shadowdogs.stat.Karma import Karma
from gdo.shadowdogs.stat.Nuyen import Nuyen
from gdo.shadowdogs.stat.Thirst import Thirst
from gdo.shadowdogs.stat.XP import XP

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.locations.City import City
    from gdo.shadowdogs.locations.Location import Location

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
from gdo.shadowdogs.item.classes.weapon.Fists import Fists
from gdo.shadowdogs.item.classes.Weapon import Weapon
from gdo.shadowdogs.skill.Aim import Aim
from gdo.shadowdogs.skill.Fight import Fight
from gdo.shadowdogs.skill.Hacking import Hacking
from gdo.shadowdogs.stat.HP import HP
from gdo.shadowdogs.stat.Level import Level
from gdo.shadowdogs.stat.MP import MP
from gdo.user.GDT_Gender import GDT_Gender


class SD_Player(WithShadowFunc, GDO):

    modified: dict[str, int]
    inventory: 'Inventory'
    party_pos: int
    distance: int
    combat_stack: CombatStack
    command_eta: int

    __slots__ = (
        'modified',
        'inventory',
        'party_pos',
        'distance',
        'combat_stack',
        'command_eta',
    )

    def __init__(self):
        super().__init__()
        self.reset_modified()
        self.inventory = Inventory()
        self.party_pos = 0
        self.distance = 0
        self.combat_stack = CombatStack(self)
        self.command_eta = 0

    def reset_modified(self):
        self.modified = {
            'p_bod': 0, 'p_mag': 0, 'p_str': 0, 'p_qui': 0, 'p_dex': 0, 'p_int': 0, 'p_wis': 0, 'p_cha': 0,
            'p_aim': 0, 'p_fig': 0, 'p_hac': 0, 'p_tra': 0,
            'p_hp': 0, 'p_mp': 0, 'p_max_hp': 0, 'p_max_mp': 0,
            'p_attack': 0, 'p_defense': 0,
            'p_min_dmg': 0, 'p_max_dmg': 0,
            'p_marm': 0, 'p_farm': 0,
            'p_alcohol': 0, 'p_hunger': 100, 'p_thirst': 100,
            'p_weight': 0, 'p_max_weight': 0,
            'p_level': 0,
        }

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
            GDT_UInt('p_karma_spent').bytes(2).not_null().initial('0').max(65535),
            Level('p_level').initial('1'),

            HP('p_hp'),
            MP('p_mp'),

            Nuyen('p_nuyen'),

            GDT_Race('p_race').not_null().npcs(),
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
            GDT_Item('p_earring'),
            GDT_Item('p_piercing'),
            GDT_Item('p_mount'),

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
            Trading('p_tra'),

            Alcohol('p_alcohol'),
            Hunger('p_hunger').initial('50'),
            Thirst('p_thirst').initial('30'),

            GDT_Created('p_created'),
        ]

    def is_npc(self) -> bool:
        return False

    def get_user(self) -> GDO_User:
        return self.gdo_value('p_user')

    def get_city(self) -> 'City':
        return self.get_party().get_city()

    def get_name(self):
        if name := self.gdo_val('p_npc_name'):
            return f"{name}[{self.get_id()}]"
        return self.get_user().render_name()

    async def is_online(self) -> bool:
        return await self.get_user().is_online()

    ##########
    # Combat #
    ##########

    def new_combat(self, enemies: 'SD_Party'):
        self.combat_stack.reset()
        return self

    async def combat_tick(self):
        await self.combat_stack.tick()

    def is_dead(self) -> bool:
        return self.g('p_hp') <= 0

    def kill(self):
        from gdo.shadowdogs.engine.Factory import Factory
        self.get_party().members.remove(self)
        party = Factory.create_party(self.get_city().get_respawn_location(self))
        party.members.append(self)
        return self.save_vals({
            'p_party': party.get_id(),
            'p_joined': Time.get_date(),
        })

    #############
    # Equipment #
    #############

    def get_weapon(self) -> 'Weapon':
        return self.get_equipment('p_weapon') or Fists()

    def get_equip(self, slot_name: str) -> 'SD_Item':
        try:
            return self.gdo_value(GDT_Slot.map(slot_name))
        except AttributeError as ex:
            return None

    def get_equipment(self, slot_name: str) -> Equipment|None:
        if item := self.get_equip(slot_name):
            return item.itm()

    ########
    # Data #
    ########

    def c(self, key: str) -> Modifier:
        return self.column(key).value(self.g(key)+self.gb(key))

    def g(self, key: str) -> int:
        return self.modified[key]

    def gb(self, key: str) -> int:
        return self.gdo_value(key)

    def s(self, key: str, value: int):
        self.modified[key] = value
        return self

    ##########
    # Modify #
    ##########

    def modify_all(self):
        self.reset_modified()
        self.column('p_race').apply(self)
        self.level_column().apply(self)
        self.column('p_faction').apply(self)
        for key in Attribute.ATTRIBUTES:
            self.c(key).apply(self)
        for key in Skill.SKILLS:
            self.c(key).apply(self)
        for slot in GDT_Slot.SLOTS:
            if item := self.gdo_value(slot):
                item.itm().apply(self)
        for item in self.inventory:
            item.itm().apply_inv(self)
        return self

    def apply(self, name: str, inc: int):
        self.modified[name] += inc
        return self

    def modify(self, stats: dict[str, int]):
        for key, val in stats.items():
            self.apply(key, val)
        return self

    def give_hp(self, hp: int):
        return self.s('p_hp', min(self.g('p_hp') + hp, self.g('p_max_hp')))

    def give_mp(self, mp: int):
        return self.s('p_mp', min(self.g('p_mp') + mp, self.g('p_max_mp')))

    def get_total_karma(self) -> int:
        return self.gdo_value('p_xp') // Shadowdogs.XP_PER_KARMA

    def give_xp(self, xp: int) -> str:
        total_karma = self.get_total_karma()
        self.increment('p_xp', xp)
        out = t('msg_sd_got_xp', (xp,))
        out += self.check_karma_xp(total_karma)
        out += self.check_level_xp()
        return out.strip()

    def check_karma_xp(self, karma_before: int) -> str:
        new_total_karma = self.get_total_karma()
        new_karma = new_total_karma - karma_before
        if new_karma > 0:
            self.increment('p_karma', new_karma)
            return " " + t('msg_sd_gained_karma', (new_karma, self.gdo_value('p_karma')))
        return ''

    def level_column(self) -> Level:
        return self.column('p_level')

    def check_level_xp(self) -> str:
        output = ''
        xp = self.gdo_value('p_xp')
        while xp >= self.level_column().xp_needed(self):
            self.increment('p_level', 1)
            level = self.gdo_value('p_level')
            xp = self.gdo_value('p_xp')
            output += " " + t('msg_sd_gained_level', (level, self.level_column().xp_needed(self) - xp, level + 1))
        return output

    def has_kp(self, location: 'Location') -> bool:
        return SD_Place.has_location(self, location)

    def hit(self, dmg: int):
        self.give_hp(-dmg)

    #########
    # Nuyen #
    #########
    def get_nuyen(self) -> int:
        return self.gb('p_nuyen')

    def has_nuyen(self, nuyen: int) -> bool:
        return self.get_nuyen() >= nuyen

    def give_nuyen(self, nuyen: int):
        return self.increment('p_nuyen', nuyen)

    def render_ny(self) -> str:
        return Shadowdogs.display_nuyen(self.get_nuyen())

    #########
    # Spell #
    #########
    def has_spell(self, spell_name: str) -> bool:
        return False

    #########
    # Party #
    #########

    def get_party(self) -> 'SD_Party':
        return self.gdo_value('p_party')

    def is_near(self, player: 'SD_Player') -> bool:
        p = self.get_party()
        ep = player.get_party()
        if p == ep:
            return True
        if p.get_target() == ep:
            return True
        if p.get_location('inside') == ep.get_location('inside'):
            return True
        if p.get_location('outside') == ep.get_location('outside'):
            return True
        return False

    def busy(self, time: int) -> str:
        self.command_eta = self.get_time() + time
        return Time.human_duration(time)
