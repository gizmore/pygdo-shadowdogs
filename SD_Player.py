from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.base.Trans import t
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from typing import TYPE_CHECKING, Generator, Any

from gdo.date.Time import Time
from gdo.math.GDT_RandomSeed import GDT_RandomSeed
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.SD_Place import SD_Place
from gdo.shadowdogs.GDT_RandomName import GDT_RandomName
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.attr.Magic import Magic
from gdo.shadowdogs.engine.CombatStack import CombatStack
from gdo.shadowdogs.engine.Modifier import Modifier
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.item.classes.Equipment import Equipment
from gdo.shadowdogs.skill.Math import Math
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
from gdo.shadowdogs.skill.Math import Math
from gdo.shadowdogs.stat.HP import HP
from gdo.shadowdogs.stat.Level import Level
from gdo.shadowdogs.stat.MP import MP
from gdo.user.GDT_Gender import GDT_Gender


class SD_Player(WithShadowFunc, GDO):

    modified: dict[str, int]
    inventory: 'Inventory'
    mount: 'Inventory'
    bank: 'Inventory'
    bazaar: 'Inventory'
    cyberware: 'Inventory'
    cyberdeck: 'Inventory'
    party_pos: int
    distance: int
    combat_stack: CombatStack

    __slots__ = (
        'modified',
        'inventory',
        'mount',
        'bank',
        'bazaar',
        'cyberware',
        'cyberdeck',
        'party_pos',
        'distance',
        'combat_stack',
    )

    STATS = (
        'p_level',
    )

    def __init__(self):
        super().__init__()
        self.reset_modified()
        self.inventory = Inventory()
        self.mount = Inventory()
        self.bank = Inventory()
        self.bazaar = Inventory()
        self.cyberware = Inventory()
        self.cyberdeck = Inventory()
        self.party_pos = 0
        self.distance = 0
        self.command_eta = 0
        self.combat_stack = CombatStack(self)

    def reset_modified(self):
        self.modified = {
            'p_bod': 0, 'p_mag': 0, 'p_str': 0, 'p_qui': 0, 'p_dex': 0, 'p_int': 0, 'p_wis': 0, 'p_cha': 0,
            'p_aim': 0, 'p_fig': 0, 'p_hac': 0, 'p_tra': 0, 'p_mat': 0,
            'p_surveil': 0, 'p_cpu': 0, 'p_mcpu': 0,
            'p_max_hp': 0, 'p_max_mp': 0,
            'p_attack': 0, 'p_defense': 0, 'p_at': 50,
            'p_min_dmg': 0, 'p_max_dmg': 0,
            'p_marm': 0, 'p_farm': 0,
            'p_alcohol': 0, 'p_hunger': 100, 'p_thirst': 100,
            'p_weight': 0, 'p_max_weight': 0,
            'p_level': 0,
            'p_xp': 0, 'p_karma': 0,
            'p_nuyen': 0, 'p_bank_nuyen': 0,
        }
        if 'p_hp' not in self.modified:
            self.modified['p_hp'] = 0
        if 'p_mp' not in self.modified:
            self.modified['p_mp'] = 0

    def gdo_columns(self) -> list[GDT]:
        from gdo.shadowdogs.GDT_NPCClass import GDT_NPCClass
        return [
            GDT_AutoInc('p_id'),

            GDT_User('p_user'),

            GDT_Party('p_party'),
            GDT_UInt('p_joined').bytes(8),

            GDT_RandomSeed('p_seed').init_random().not_null(),

            GDT_NPCClass('p_npc_class'),
            GDT_RandomName('p_npc_name'),

            XP('p_xp'),
            Karma('p_karma'),
            GDT_UInt('p_karma_spent').bytes(2).not_null().initial('0').max(65535),
            Level('p_level').initial('1'),

            HP('p_hp'),
            MP('p_mp'),

            Nuyen('p_nuyen'),
            Nuyen('p_nuyen_bank'),

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
            GDT_Item('p_cyberdeck'),

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
            Math('p_mat'),

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
        return self.get_user().render_name()

    def is_online(self) -> bool:
        return self.get_user().is_online()

    def is_leader(self) -> bool:
        return self.get_party().get_leader() == self

    ##########
    # Combat #
    ##########

    async def combat_tick(self):
        await self.combat_stack.tick()

    def new_combat(self, enemies: 'SD_Party'):
        self.combat_stack.reset()
        return self

    def hit(self, dmg: int):
        self.give_hp(-dmg)
        return self

    def is_dead(self) -> bool:
        return self.g('p_hp') <= 0

    def is_alive(self) -> bool:
        return not self.is_dead()

    async def kill(self):
        from gdo.shadowdogs.engine.Factory import Factory
        location = self.get_city().get_respawn_location(self)
        self.get_party().members.remove(self)
        party = await Factory.create_party(location)
        party.members.append(self)
        return self.save_vals({
            'p_party': party.get_id(),
            'p_joined': str(self.get_time()),
        })

    ########
    # Hack #
    ########
    def all_programs(self) -> Generator[Item, Any, None]:
        for program in self.cyberdeck:
            yield program.itm()


    #############
    # Equipment #
    #############
    def all_equipment(self) -> Generator[Item, Any, None]:
        for slot_name in GDT_Slot.SLOTS:
            if item := self.get_equipment(slot_name):
                yield item
        for item in self.cyberware:
            yield item.itm()
        yield from self.all_programs()

    def get_weapon(self) -> 'Weapon':
        return self.get_equipment('p_weapon') or Fists().player(self)

    def get_equip(self, slot_name: str) -> 'SD_Item|None':
        try:
            return self.gdo_value(GDT_Slot.map(slot_name))
        except AttributeError as ex:
            return None

    def get_equipment(self, slot_name: str) -> 'Equipment|Item|None':
        if item := self.get_equip(slot_name):
            return item.itm()
        return None

    ########
    # Busy #
    ########
    def busy(self, seconds: int):
        self.combat_stack.busy(seconds)
        return self

    def is_busy(self) -> bool:
        return self.combat_stack.is_busy()

    def render_busy(self) -> str:
        if not self.is_busy():
            return ''
        return " " + t('sd_busy', (Time.human_duration(self.combat_stack.get_busy_seconds()),))

    def get_busy_seconds(self) -> int:
        return self.combat_stack.get_busy_seconds()

    ########
    # Data #
    ########

    def c(self, key: str) -> Modifier|GDT:
        return self.column(key).value(self.g(key))

    def g(self, key: str) -> int:
        """
        Get modified value
        """
        return self.modified[key]

    def gb(self, key: str) -> int:
        """
        Get Base value
        """
        return self.gdo_value(key)

    def s(self, key: str, value: int):
        self.modified[key] = value
        return self

    ###########
    # Methods #
    ###########

    def get_sd_methods(self) -> list[str]:
        methods = []
        for item in self.all_items():
            methods.extend(item.sd_commands())
        return methods

    #########
    # Items #
    #########

    def all_items(self) -> Generator[Item, Any, None]:
        yield from self.all_equipment()
        for item in self.inventory:
            yield item.itm()

    ##########
    # Modify #
    ##########

    def modify_all(self):
        self.reset_modified()
        for key, value in self.modified.items():
            if key in self._vals:
                self.apply(key, self.gdo_value(key))
        self.column('p_race').apply(self)
        self.column('p_faction').apply(self)
        self.level_column().apply(self)
        for slot in GDT_Slot.SLOTS:
            if item := self.gdo_value(slot):
                item.itm().apply(self)
        for item in self.inventory:
            item.itm().apply_inv(self)
        for key in Attribute.ATTRIBUTES:
            self.c(key).apply(self)
        for key in Skill.SKILLS:
            self.c(key).apply(self)
        return self

    def apply(self, name: str, inc: int):
        self.modified[name] += inc
        return self

    def modify(self, stats: dict[str, int]):
        for key, val in stats.items():
            self.apply(key, val)
        return self

    def digesting(self):
        pass

    #########
    # HP/MP #
    #########

    def give_hp(self, hp: int):
        return self.s('p_hp', min(self.g('p_hp') + hp, self.g('p_max_hp')))

    def give_mp(self, mp: int):
        return self.s('p_mp', min(self.g('p_mp') + mp, self.g('p_max_mp')))

    def heal_full(self):
        self.give_hp(self.g('p_max_hp'))
        self.give_mp(self.g('p_max_mp'))
        return self

    ######
    # XP #
    ######

    def level_column(self) -> Level|GDT:
        return self.column('p_level')

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

    def check_level_xp(self) -> str:
        output = ''
        xp = self.gdo_value('p_xp')
        while xp >= self.level_column().xp_needed(self):
            self.increment('p_level', 1)
            level = self.gdo_value('p_level')
            xp = self.gdo_value('p_xp')
            output += " " + t('msg_sd_gained_level', (level, self.level_column().xp_needed(self) - xp, level + 1))
        return output

    #########
    # Nuyen #
    #########
    def has_nuyen(self, nuyen: int) -> bool:
        return self.get_nuyen() >= nuyen

    def get_nuyen(self) -> int:
        return self.gb('p_nuyen')

    def give_nuyen(self, nuyen: int):
        return self.increment('p_nuyen', nuyen)

    def render_ny(self) -> str:
        return Shadowdogs.display_nuyen(self.get_nuyen())

    ##########
    # Places #
    ##########
    def has_kp(self, location: 'Location') -> bool:
        return SD_Place.has_location(self, location)

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

    #######
    # NPC #
    #######
    def as_real_class(self):
        return self

    ##########
    # Render #
    ##########
    def render_gender(self):
        self.column('p_gender').render_txt()

    def render_race(self):
        self.column('p_race').render_txt()
