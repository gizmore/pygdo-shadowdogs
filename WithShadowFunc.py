from typing import TYPE_CHECKING

from gdo.base.Application import Application
from gdo.base.GDT import GDT
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Render import Render
from gdo.base.Util import Strings, gdo_print
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
    from gdo.shadowdogs.locations.Bank import Bank
    from gdo.shadowdogs.SD_KnownWord import SD_KnownWord
    from gdo.shadowdogs.locations.Location import Location
    from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.item.Item import Item
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.SD_Spell import SD_Spell
    from gdo.shadowdogs.SD_Place import SD_Place
    from gdo.shadowdogs.engine.MethodSD import MethodSD
    from gdo.shadowdogs.actions.Action import Action
    from gdo.shadowdogs.locations.School import School
    from gdo.shadowdogs.locations.Store import Store

from gdo.base.Trans import Trans, t


class WithShadowFunc(WithPlayerGDO):

    Loader = None
    module_shadowdogs = None

    @classmethod
    def mod_sd(cls) -> 'module_shadowdogs':
        if not cls.module_shadowdogs:
            from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
            cls.module_shadowdogs = module_shadowdogs
        return cls.module_shadowdogs.instance()

    def nearby_players(self, player: 'SD_Player', same: bool = False):
        return player.get_party().players_nearby(player if not same else None)

    def get_time(self) -> int:
        return int(Application.TIME)

    ############
    # Entities #
    ############

    def get_party(self) -> 'SD_Party':
        return self.get_player().get_party()

    def get_location(self) -> 'Location|Store|Bank|School':
        return self.get_party().get_location()

    def get_action(self) -> 'Action':
        return self.get_party().get_action()

    def get_action_name(self) -> str:
        return self.get_action().get_name()

    ##########
    # Engine #
    ##########
    World = None
    @classmethod
    def world(cls):
        if cls.World is None:
            from gdo.shadowdogs.engine.World import World
            cls.World = World
        return cls.World

    Factory = None
    def factory(self):
        if self.__class__.Factory is None:
            from gdo.shadowdogs.engine.Factory import Factory
            self.__class__.Factory = Factory
        return self.__class__.Factory

    def get_loader(self):
        if not self.__class__.Loader:
            from gdo.shadowdogs.engine.Loader import Loader
            self.__class__.Loader = Loader
        return self.__class__.Loader

    ##########
    # Attack #
    ##########

    async def mob_attack(self, party: 'SD_Party', mob_names: str):
        ep = await self.factory().create_default_npcs(party.get_location(), mob_names)
        await party.fight(ep)

    async def npc_attack(self, *types: 'type[TalkingNPC]'):
        party = self.factory().create_party(self.get_location())
        for type in types:
            party.join_silent(type.blank().insert().modify_all().heal_full())
        await self.get_party().fight(party)

    ##########
    # Method #
    ##########

    @classmethod
    def gdo_default_enabled_channel(cls) -> bool:
        return False

    def gdo_method_hidden(self) -> bool:
        return True

    def sd_methods(self, player: 'SD_Player') -> list[str]:
        return GDT.EMPTY_LIST

    def get_method(self, name: str) -> 'MethodSD':
        return ModuleLoader.instance()._methods.get(name)

    def execute_sd_method(self, line: str) -> GDT:
        pass
        

    ############
    # Messages #
    ############

    async def send_to_player(self, player: 'SD_Player', key: str, args: tuple = None):
        if player.is_npc():
            gdo_print(self.t(key, args))
        else:
            await player.get_user().send(key, args)

    async def send_to_party(self, party: 'SD_Party', key: str, args: tuple = None):
        for player in party.members:
            await self.send_to_player(player, key, args)

    async def send_to_all(self, key: str, args: tuple[str | int | float, ...] | None = None):
        active_channels = self.get_loader().channels_with_shadowlamb()
        for player in self.nearby_players(p):
            user = player.get_user()
            for active_channel in active_channels:
                if active_channel.is_user_online(user):
                    continue
            await self.send_to_player(player, key, args)
        for active_channel in active_channels:
            await active_channel.send(self.t(key, args))

    async def broadcast(self, key: str, args: tuple = None):
        for channel in self.get_loader().channels_with_shadowlamb():
            with Trans(channel.get_lang_iso()):
                await channel.send(Trans.t(key, args))

    def t(self, key: str, args: tuple[str|int|float,...]=None):
        s = Trans.t(key, args)
        return self.replace_output(s)

    def get_sd_shortcut(self) -> str:
        return self.get_player().get_user().get_setting_val('sd_shortcut')

    def replace_output(self, text: str) -> str:
        return text.replace('$t$', self.get_sd_shortcut())

    #########
    # Items #
    #########

    async def give_new_items(self, player: 'SD_Player', item_name: str, announce_action: str=None, announce_source: str=None):
        items = []
        for iname in item_name.split(Shadowdogs.ITEM_SEPERATOR):
            item_count = 1
            if iname[0].isdigit():
                item_count = int(Strings.substr_to(iname, Shadowdogs.ITEM_COUNT_SEPERATOR, 1))
                iname = Strings.substr_from(iname, Shadowdogs.ITEM_COUNT_SEPERATOR, iname)
            item = self.factory().create_item(Strings.substr_to(iname, Shadowdogs.MODIFIER_SEPERATOR, iname),
                            item_count,
                            Strings.substr_from(item_name, Shadowdogs.MODIFIER_SEPERATOR))
            items.append(item)
        if items:
            await self.give_items(player, items, announce_action, announce_source)

    async def give_items(self, player: 'SD_Player', items: 'list[Item]', announce_action: str=None, announce_source: str=None):
        for item in items:
            await self.give_item(player, item)
        if announce_action:
            item_names = ', '.join([item.render_name() for item in items])
            await self.send_to_party(player.get_party(), f'sd_receive_item_{announce_action}', (item_names, announce_source))

    async def give_item(self, player: 'SD_Player', item: 'Item', announce_action: str=None, announce_source: str=None):
        await player.on_give(item)
        if announce_action:
            await self.send_to_party(player.get_party(), f'sd_receive_item_{announce_action}', (item.render_name(), announce_source))

    ######
    # XP #
    ######
    async def give_xp(self, player: 'SD_Player', xp: int):
        await player.give_xp(xp, True)

    ######
    # KP #
    ######
    async def give_kp(self, player: 'SD_Player', location: 'Location', announce: bool=True):
        from gdo.shadowdogs.SD_Place import SD_Place
        party = player.get_party()
        for member in party.members:
            if not member.has_kp(location):
                SD_Place.give_place(member, location)
                if announce:
                    await self.send_to_player(player, 'msg_sd_new_kp', (location.get_city().get_name(), location.get_name(), location.render_descr(player)))

    async def give_party_kp(self, party: 'SD_Party', location: 'Location', announce: bool=True):
        for member in party.members:
            await self.give_kp(member, location, announce)

    #########
    # Words #
    #########
    async def give_word(self, player: 'SD_Player', word: str, announce: bool=True):
        from gdo.shadowdogs.SD_KnownWord import SD_KnownWord
        if not SD_KnownWord.has_word(player, word):
            SD_KnownWord.give_word(player, word)
            if announce:
                await self.send_to_player(player, 'msg_sd_new_word', (Render.bold(word),))

    ##########
    # Spells #
    ##########
    def has_spell(self, player: 'SD_Player', spell: str) -> bool:
        from gdo.shadowdogs.SD_Spell import SD_Spell
        return SD_Spell.get_for_player(player, spell) is not None

    async def give_spell(self, player: 'SD_Player', spell: str, announce: str=None):
        from gdo.shadowdogs.SD_Spell import SD_Spell
        if not self.has_spell(player, spell):
            SD_Spell.create_for_player(player, spell)
            if announce:
                await self.send_to_player(player, 'msg_sd_new_spell', (t('sd_spell_'+spell), t(announce)))
