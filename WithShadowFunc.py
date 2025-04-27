import functools
from typing import TYPE_CHECKING

import aioconsole

from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import Strings
from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs

if TYPE_CHECKING:
    from gdo.shadowdogs.locations.Location import Location
    from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.SD_Item import SD_Item
    from gdo.shadowdogs.SD_Party import SD_Party
    from gdo.shadowdogs.SD_Place import SD_Place
    from gdo.shadowdogs.engine.MethodSD import MethodSD

from gdo.base.Trans import Trans, t
from gdo.core.GDO_Channel import GDO_Channel


class WithShadowFunc:

    _player: 'SD_Player'

    @classmethod
    def mod_sd(cls) -> 'module_shadowdogs':
        from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
        return module_shadowdogs.instance()

    @classmethod
    def get_time(cls) -> int:
        return cls.mod_sd().cfg_time()

    ############
    # Entities #
    ############

    def player(self, player: 'SD_Player'):
        self._player = player
        return self

    def get_player(self, user: GDO_User=None) -> 'SD_Player':
        if hasattr(self, '_player'):
            return self._player
        from gdo.shadowdogs.SD_Player import SD_Player
        user = user or self._env_user
        return SD_Player.table().get_by('p_user', user.get_id())

    def get_party(self) -> 'SD_Party':
        return self.get_player().get_party()

    def get_location(self) -> 'Location':
        return self.get_party().get_location()

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
        from gdo.shadowdogs.method.stats import stats
        for channel in GDO_Channel.with_setting(stats(), 'disabled', '0', '1'):
            with Trans(channel.get_lang_iso()):
                await channel.send(Trans.t(key, args))

    def t(self, key: str, args: tuple[str|int|float,...]=None):
        return Trans.t(key, args)

    #########
    # Items #
    #########

    async def give_new_items(self, player: 'SD_Player', items: dict[str,int], announce_action: str=None, announce_source: str=None):
        for item_name, count in items.items():
            await self.give_new_item(player, item_name, count, announce_action, announce_source)

    async def give_new_item(self, player: 'SD_Player', item_name: str, item_count: int, announce_action: str=None, announce_source: str=None):
        from gdo.shadowdogs.engine.Factory import Factory
        item = Factory.create_item(Strings.substr_to(item_name, Shadowdogs.MODIFIER_SEPERATOR, item_name),
                            item_count,
                            Strings.substr_from(item_name, Shadowdogs.MODIFIER_SEPERATOR))
        await self.give_item(player, item, announce_action, announce_source)

    async def give_item(self, player: 'SD_Player', item: 'SD_Item', announce_action: str=None, announce_source: str=None):
        item.save_vals({
            'item_owner': player.get_id(),
            'item_slot': 'inventory',
        })
        player.inventory.append(item)
        if announce_action:
            await self.send_to_party(player.get_party(), f'sd_receive_item_{announce_action}', (item.render_name(), announce_source,))

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
