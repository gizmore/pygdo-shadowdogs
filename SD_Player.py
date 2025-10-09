from gdo.base.Cache import Cache
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_User import GDT_User
from gdo.date.GDT_Created import GDT_Created
from typing import TYPE_CHECKING, Generator, Any, Self

from gdo.shadowdogs.GDT_NPCClass import GDT_NPCClass
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.item.classes.Nuyen import Nuyen as NY

from gdo.date.Time import Time
from gdo.math.GDT_RandomSeed import GDT_RandomSeed
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.GDT_RandomName import GDT_RandomName
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.attr.Luck import Luck
from gdo.shadowdogs.attr.Magic import Magic
from gdo.shadowdogs.engine.CombatStack import CombatStack
from gdo.shadowdogs.engine.Modifier import Modifier
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.item.classes.Equipment import Equipment
from gdo.shadowdogs.skill.Crypto import Crypto
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
    from gdo.shadowdogs.engine.Loot import Loot

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
    _combat_stack: CombatStack

    Loot = None
    def loot(self) -> 'type[Loot]':
        if self.__class__.Loot is None:
            from gdo.shadowdogs.engine.Loot import Loot
            self.__class__.Loot = Loot
        return self.__class__.Loot

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
        '_combat_stack',
    )

    def __init__(self):
        super().__init__()
        self.inventory = Inventory()
        self.mount = Inventory()
        self.bank = Inventory()
        self.bazaar = Inventory()
        self.cyberware = Inventory()
        self.cyberdeck = Inventory()
        self.party_pos = 0
        self.distance = 0
        self.command_eta = 0
        self.modified = {}
        self._combat_stack = None

    def combat_stack(self) -> CombatStack:
        if self._combat_stack is None:
            self._combat_stack = CombatStack(self)
        return self._combat_stack

    def reset_modified(self):
        self.modified.update({
            'p_bod': 0, 'p_mag': 0, 'p_str': 0, 'p_qui': 0, 'p_dex': 0, 'p_int': 0, 'p_wis': 0, 'p_cha': 0, 'p_luc': 0,
            'p_aim': 0, 'p_fig': 0, 'p_hac': 0, 'p_tra': 0, 'p_mat': 0, 'p_cry': 0,
            'p_surveil': 0, 'p_cpu': 0, 'p_mcpu': 0,
            'p_max_hp': 0, 'p_max_mp': 0,
            'p_attack': 0, 'p_defense': 0, 'p_at': 50,
            'p_min_dmg': 0, 'p_max_dmg': 0,
            'p_marm': 0, 'p_farm': 0,
            'p_weight': 0, 'p_max_weight': 0,
            'p_level': 0,
            'p_hunger': 0, 'p_thirst': 0, 'p_alcohol': 0,
        })
        return self

    def gdo_table_name(cls) -> str:
        return 'sd_player'

    def on_reload(self):
        super().on_reload()

    @classmethod
    def gdo_real_class(cls, vals: dict[str,str]) -> type[GDO]:
        from gdo.shadowdogs.npcs.npcs import npcs
        if klass := vals.get('p_npc_class'):
            print(klass)
            return GDT_NPCClass.TALKING_NPCS.get(klass, npcs.get_class(klass))
        return cls

    @classmethod
    def gdo_base_class(cls) -> type[GDO]:
        return SD_Player

    def gdo_columns(self) -> list[GDT]:
        from gdo.shadowdogs.GDT_NPCClass import GDT_NPCClass
        return [
            GDT_AutoInc('p_id'),

            GDT_User('p_user'),

            GDT_Party('p_party').cascade_delete(),
            GDT_UInt('p_joined').bytes(8),

            GDT_RandomSeed('p_seed').init_random().not_null(),

            GDT_NPCClass('p_npc_class'),
            GDT_RandomName('p_npc_name'),

            XP('p_xp'),
            GDT_UInt('p_xp_karma').initial('0').not_null(),
            Karma('p_karma'),
            GDT_UInt('p_karma_spent').bytes(2).not_null().initial('0').max(65535),
            Level('p_level').initial('1'),

            HP('p_hp'),
            MP('p_mp'),

            Nuyen('p_nuyen'),
            Nuyen('p_bank_nuyen'),

            GDT_Race('p_race').not_null().npcs(),
            GDT_Gender('p_gender').simple().not_null(),
            GDT_Faction('p_faction').initial(GDT_Faction.SEEKER).not_null(),

            GDT_Item('p_weapon').cascade_delete(),
            GDT_Item('p_armor').cascade_delete(),
            GDT_Item('p_trousers').cascade_delete(),
            GDT_Item('p_helmet').cascade_delete(),
            GDT_Item('p_boots').cascade_delete(),
            GDT_Item('p_gloves').cascade_delete(),
            GDT_Item('p_amulet').cascade_delete(),
            GDT_Item('p_ring').cascade_delete(),
            GDT_Item('p_earring').cascade_delete(),
            GDT_Item('p_piercing').cascade_delete(),
            GDT_Item('p_mount').cascade_delete(),
            GDT_Item('p_cyberdeck').cascade_delete(),

            Body('p_bod'),
            Magic('p_mag'),
            Strength('p_str'),
            Quickness('p_qui'),
            Dexterity('p_dex'),
            Intelligence('p_int'),
            Wisdom('p_wis'),
            Charisma('p_cha'),
            Luck('p_luc'),

            Aim('p_aim'),
            Fight('p_fig'),
            Hacking('p_hac'),
            Trading('p_tra'),
            Math('p_mat'),
            Crypto('p_cry'),

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

    ########
    # Chat #
    ########
    async def on_say(self, player: 'SD_Player', word: str):
        pass

    ##########
    # Combat #
    ##########

    async def combat_tick(self):
        await self.combat_stack().tick()

    def new_combat(self, enemies: 'SD_Party'):
        self.combat_stack().reset()
        return self

    def hit(self, dmg: int):
        self.give_hp(-dmg)
        return self

    def is_dead(self) -> bool:
        return self.gb('p_hp') <= 0

    def is_alive(self) -> bool:
        return not self.is_dead()

    async def kill(self, killer: 'SD_Player'):
        if killer:
            loot = self.loot()
            await loot(killer, self).on_kill()

        old_party = self.get_party()
        old_party.members.remove(self)

        if not (location := self.get_city().get_respawn_location(self)):
            if old_party.is_empty(): # MOB + Empty
                old_party.delete()
                return self
            else:
                return self.delete() # Mob

        if old_party.is_empty(): # Human Empty
            await old_party.do(Action.INSIDE, location.get_location_key())
            old_party.join_silent(self)
            return self
        else: # Human respawn
            party = self.factory().create_party(location)
            party.members.append(self)
            self.party_pos = 1
            self.save_vals({
                'p_party': party.get_id(),
                'p_joined': str(self.get_time()),
            })
            return self

    ########
    # Hack #
    ########
    def all_programs(self) -> Generator[SD_Item, Any, None]:
        for program in self.cyberdeck:
            yield program

    #############
    # Equipment #
    #############
    def all_equipment(self) -> Generator[SD_Item, Any, None]:
        for slot_name in GDT_Slot.SLOTS:
            if item := self.get_equipment(slot_name):
                yield item
        yield from self.cyberware

    def get_weapon(self) -> 'Weapon':
        return self.get_equipment('p_weapon') or Fists().fill_defaults({'item_name': 'Fists', 'item_owner': self.get_id()}).player(self)

    def get_equipment(self, slot_name: str) -> 'SD_Item|None':
        try:
            return self.gdo_value(slot_name)
        except AttributeError as ex:
            return None

    # def unequip(self, item: 'SD_Item'):
    #     self.save_val(item.get_slot(), None)
    #     return self

    ########
    # Busy #
    ########
    def busy(self, seconds: int):
        self.combat_stack().busy(seconds)
        return self

    def is_busy(self) -> bool:
        return self.combat_stack().is_busy()

    def render_busy(self) -> str:
        if not self.is_busy():
            return ''
        return " " + t('sd_busy', (Time.human_duration(self.combat_stack().get_busy_seconds()),))

    def get_busy_seconds(self) -> int:
        return self.combat_stack().get_busy_seconds()

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

    def sb(self, key: str, value: int):
        return self.set_value(key, value)


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

    def all_items(self) -> Generator[SD_Item, Any, None]:
        yield from self.all_equipment()
        yield from self.inventory

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
                item.apply(self)
        if not self.get_equipment('p_weapon'):
            self.get_weapon().apply(self)
        for item in self.inventory:
            item.apply_inv(self)
        for key in Attribute.ATTRIBUTES:
            self.c(key).apply(self)
        for key in Skill.SKILLS:
            self.c(key).apply(self)
        return self

    def apply(self, name: str, inc: int) -> Self:
        self.modified[name] += inc
        return self

    def inc(self, key: str, by: int):
        gdt = self.column(key)
        old = self.modified.get(key)
        new = old + by
        if gdt._min is not None and new < gdt._min:
            new = gdt._min
        if gdt._max is not None and new > gdt._max:
            new = gdt._max
        self.modified[key] = new
        return self

    def incb(self, key: str, by: int):
        gdt = self.column(key)
        old = self.gb(key)
        new = old + by
        if gdt._min is not None and new < gdt._min:
            new = gdt._min
        if gdt._max is not None and new > gdt._max:
            new = gdt._max
        self.sb(key, new)
        return self

    def modify(self, stats: dict[str, int]):
        for key, val in stats.items():
            self.apply(key, val)
        return self

    ########
    # Food #
    ########

    async def digesting(self):
        self.incb('p_hunger', -Shadowdogs.FOOD_PER_TICK)
        self.incb('p_thirst', -Shadowdogs.WATER_PER_TICK)
        dmg = 0
        if self.gb('p_hunger') == 0:
            dmg += 1
        if self.gb('p_thirst') == 0:
            dmg += 1
        if dmg:
            self.give_hp(-dmg)
            await self.send_to_player(self, 'msg_sd_not_saturated', (dmg, self.gb('p_hp'), self.g('p_max_hp')))

    #########
    # HP/MP #
    #########

    def give_hp(self, hp: int):
        return self.sb('p_hp', max(0, min(self.gb('p_hp') + hp, self.g('p_max_hp'))))

    def give_mp(self, mp: int):
        return self.sb('p_mp', max(0, min(self.gb('p_mp') + mp, self.g('p_max_mp'))))

    def heal_full(self):
        self.give_hp(self.g('p_max_hp'))
        self.give_mp(self.g('p_max_mp'))
        return self

    ######
    # XP #
    ######

    def level_column(self) -> Level|GDT:
        return self.column('p_level')

    def get_xp_per_karma(self) -> int:
        return Shadowdogs.XP_PER_KARMA + Shadowdogs.XP_PER_KARMA_PER_LEVEL * self.gb('p_level')

    async def give_xp(self, xp: int, force_msg: bool=False) -> str:
        out = ""
        out += self.check_karma_xp(xp)
        out += self.check_level_xp(xp)
        out = out.strip()
        if out or force_msg:
            await self.send_to_player(self, 'msg_sd_gain_xp', (xp, out,))
        return out.strip()

    def check_karma_xp(self, xp: int) -> str:
        self.increment('p_xp', xp).increment('p_xp_karma', xp)
        xp_need = self.get_xp_per_karma()
        karma_gain = 0
        while self.gb('p_xp_karma') >= xp_need:
            self.increment('p_xp_karma', -xp_need)
            karma_gain += 1
        if karma_gain:
            self.increment('p_karma', karma_gain)
            return " " + t('msg_sd_gained_karma', (karma_gain, self.gdo_value('p_karma')))
        return ''

    def check_level_xp(self, xp: int) -> str:
        output = ''
        xp = self.gdo_value('p_xp')
        while xp >= self.level_column().xp_needed(self):
            self.increment('p_level', 1)
            level = self.gdo_value('p_level')
            xp = self.gdo_value('p_xp')
            output += " " + t('msg_sd_gained_level', (level,))
        return output

    #########
    # Nuyen #
    #########
    def has_nuyen(self, nuyen: int) -> bool:
        return self.get_nuyen() >= nuyen

    def get_nuyen(self) -> int:
        item = self.inventory.get_by_name('Nuyen') or NY().name('Nuyen')
        return item.get_count()

    def give_nuyen(self, nuyen: int):
        item = self.inventory.get_by_name('Nuyen') or NY().name('Nuyen').slot(GDT_Slot.INVENTORY)
        item.increment('item_count', nuyen)
        if item.get_count() <= 0:
            self.inventory.remove(item)
            item.delete()
        return self

    def get_bank_nuyen(self) -> int:
        return self.gb('p_bank_nuyen')

    def give_bank_nuyen(self, nuyen: int):
        return self.set_value('p_bank_nuyen', nuyen)

    ##########
    # Places #
    ##########
    def has_kp(self, location: 'Location') -> bool:
        from gdo.shadowdogs.SD_Place import SD_Place
        return SD_Place.has_location(self, location)

    #########
    # Spell #
    #########

    #########
    # Party #
    #########

    def get_party(self) -> 'SD_Party':
        return self.gdo_value('p_party')

    def is_near(self, player: 'SD_Player') -> bool:
        p = self.get_party()
        ep = player.get_party()
        if p is None:
            self.get_party()
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
        from gdo.shadowdogs.npcs.npcs import npcs
        if npc_klass := self.gdo_val('p_npc_class'):
            npc = npcs.NPCS[npc_klass]['klass']()
            npc._vals = self._vals
            npc._blank = False
            Cache.OCACHE[npc.get_id()] = npc
            return npc.all_dirty(False)
        else:
            return self

    ##########
    # Render #
    ##########
    def render_gender(self):
        return self.column('p_gender').render_txt()

    def render_race(self):
        return self.column('p_race').render_txt()
