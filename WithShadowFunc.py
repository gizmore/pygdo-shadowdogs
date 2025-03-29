from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from gdo.shadowdogs.locations.Location import Location
    from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
    from gdo.shadowdogs.GDO_Player import GDO_Player
    from gdo.shadowdogs.GDO_Item import GDO_Item
    from gdo.shadowdogs.GDO_Party import GDO_Party
    from gdo.shadowdogs.GDO_KnownPlaces import GDO_KnownPlaces

from gdo.base.Trans import Trans
from gdo.core.GDO_Channel import GDO_Channel


class WithShadowFunc:

    def mod_sd(self) -> 'module_shadowdogs':
        from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
        return module_shadowdogs.instance()

    def get_player(self) -> 'GDO_Player':
        from gdo.shadowdogs.GDO_Player import GDO_Player
        return GDO_Player.table().get_by_aid(self._env_user.get_id())

    def get_party(self) -> 'GDO_Party':
        return self.get_player().get_party()

    def get_location(self) -> 'Location':
        return self.get_party().get_location()

    @classmethod
    def gdo_default_enabled_channel(cls) -> bool:
        return False

    def gdo_method_hidden(self) -> bool:
        return True

    ############
    # Messages #
    ############

    def send_to_player(self, player: 'GDO_Player', key: str, args: tuple[str] = None):
        player.get_user().send(key, args)

    def send_to_party(self, party: 'GDO_Party', key: str, args: tuple[str] = None):
        for player in party.members:
            self.send_to_player(player, key, args)

    def broadcast(self, key: str, args: tuple[str] = None):
        for channel in GDO_Channel.with_setting('disabled', '0', '1'):
            with Trans(channel.get_lang_iso()):
                channel.send(Trans.t(key, args))

    #########
    # Items #
    #########

    def give_items(self, player: 'GDO_Player', items: dict[str,int]):
        for item_name, count in items.items():
            self.give_item(player, item_name, count)

    def give_item(self, player: 'GDO_Player', item_name: str, item_count: int):
        from gdo.shadowdogs.GDO_Item import GDO_Item
        item = GDO_Item.create(item_name, item_count, player)
        player.inventory.append(item)
        self.send_to_player(player, 'sd_item_received', (item_name,))

    ######
    # KP #
    ######

    def give_kp(self, player: 'GDO_Player', location: 'Location'):
        party = player.get_party()
        for member in party.members:
            if not member.has_kp(location):
                self.send_to_player(player, 'msg_sd_new_kp', (location.get_city().get_name(), location.get_name()))
                GDO_KnownPlaces.give_kp(player, location)
