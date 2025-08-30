from typing import TYPE_CHECKING
from unicodedata import digit

import aioconsole

from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import Strings
from gdo.shadowdogs.WithPlayerGDO import WithPlayerGDO
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_KnownWord import SD_KnownWord
    from gdo.shadowdogs.SD_Word import SD_Word
    from gdo.shadowdogs.locations.Location import Location
    from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_Item import SD_Item
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.SD_Spell import SD_Spell
    from gdo.shadowdogs.SD_Place import SD_Place
    from gdo.shadowdogs.engine.MethodSD import MethodSD
    from gdo.shadowdogs.actions.Action import Action
    from gdo.shadowdogs.spells.Spell import Spell

from gdo.base.Trans import Trans, t
from gdo.core.GDO_Channel import GDO_Channel


class WithShadowFunc(WithPlayerGDO):

    @classmethod
    def mod_sd(cls) -> 'module_shadowdogs':
        from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
        return module_shadowdogs.instance()

    @classmethod
    def get_time(cls) -> int:
        return cls.mod_sd().cfg_time()

    def nearby_players(self, player: 'SD_Player'):
        return player.get_party().players_nearby()

    ############
    # Entities #
    ############

    def get_party(self) -> 'SD_Party':
        return self.get_player().get_party()

    def get_location(self) -> 'Location':
        return self.get_party().get_location()

    def get_action(self) -> 'Action':
        return self.get_party().get_action()

    def get_action_name(self) -> str:
        return self.get_action().get_name()

    ##########
    # Method #
    ##########

    @classmethod
    def gdo_default_enabled_channel(cls) -> bool:
        return False

    def gdo_method_hidden(self) -> bool:
        return True

    def get_method(self, name: str) -> 'MethodSD':
        return ModuleLoader.instance()._methods.get(name)

    ############
    # Messages #
    ############

    async def send_to_player(self, player: 'SD_Player', key: str, args: tuple = None):
        if player.is_npc():
            await aioconsole.aprint(t(key, args))
        else:
            await player.get_user().send(key, args)

    async def send_to_party(self, party: 'SD_Party', key: str, args: tuple = None):
        for player in party.members:
            await self.send_to_player(player, key, args)

    async def broadcast(self, key: str, args: tuple = None):
        from gdo.shadowdogs.method.info.stats import stats
        for channel in GDO_Channel.with_setting(stats(), 'disabled', '0', '1'):
            with Trans(channel.get_lang_iso()):
                await channel.send(Trans.t(key, args))

    def t(self, key: str, args: tuple[str|int|float,...]=None):
        return Trans.t(key, args)

    #########
    # Items #
    #########

    async def give_new_items(self, player: 'SD_Player', item_name: str, announce_action: str=None, announce_source: str=None):
        from gdo.shadowdogs.engine.Factory import Factory
        items = []
        for iname in item_name.split(Shadowdogs.ITEM_SEPERATOR):
            item_count = 1
            if iname[0].isdigit():
                item_count = int(Strings.substr_to(iname, Shadowdogs.ITEM_COUNT_SEPERATOR, 1))
                iname = Strings.substr_from(iname, Shadowdogs.ITEM_COUNT_SEPERATOR, iname)
            if iname == 'Nuyen':
                player.give_nuyen(item_count)
            else:
                item = Factory.create_item(Strings.substr_to(iname, Shadowdogs.MODIFIER_SEPERATOR, iname),
                                item_count,
                                Strings.substr_from(item_name, Shadowdogs.MODIFIER_SEPERATOR))
                items.append(item)
        if items:
            await self.give_items(player, items, announce_action, announce_source)

    async def give_items(self, player: 'SD_Player', items: list['SD_Item'], announce_action: str=None, announce_source: str=None):
        for item in items:
            await self.give_item(player, item)
        if announce_action:
            item_names = ''.join([item.render_name() for item in items])
            await self.send_to_party(player.get_party(), f'sd_receive_item_{announce_action}', (item_names, announce_source))

    async def give_item(self, player: 'SD_Player', item: 'SD_Item', announce_action: str=None, announce_source: str=None):
        item.set_vals({
            'item_owner': player.get_id(),
            'item_slot': item.itm().sd_inv_type(),
        })
        player.inventory.add_item(item)
        if announce_action:
            await self.send_to_party(player.get_party(), f'sd_receive_item_{announce_action}', (item.render_name(), announce_source))

    ######
    # KP #
    ######

    async def give_kp(self, player: 'SD_Player', location: 'Location', announce: bool=True):
        from gdo.shadowdogs.SD_Place import SD_Place
        party = player.get_party()
        for member in party.members:
            if not member.has_kp(location):
                SD_Place.give_kp(player, location)
                if announce:
                    await self.send_to_player(player, 'msg_sd_new_kp', (location.get_city().get_name(), location.get_name()))

    #########
    # Words #
    #########
    async def give_word(self, player: 'SD_Player', word: str, announce: bool=True):
        from gdo.shadowdogs.SD_KnownWord import SD_KnownWord
        from gdo.shadowdogs.SD_Word import SD_Word
        word = SD_Word.get_or_create(word)
        if not SD_KnownWord.has_word(player, word):
            SD_KnownWord.give_word(player, word)
            if announce:
                await self.send_to_player(player, 'msg_sd_new_word', (word.get_name(),))

    ##########
    # Spells #
    ##########
    def has_spell(self, player: 'SD_Player', spell: 'Spell', announce: bool=True) -> bool:
        return SD_Spell.get_for_player(player, spell) is not None

    async def give_spell(self, player: 'SD_Player', spell: 'Spell', announce: bool=True):
        if not self.has_spell(player, spell, announce):
            SD_Spell.create_for_player(player, spell)
            if announce:
                await self.send_to_player(player, 'msg_sd_new_spell', (spell.render_name(),))
