from gdo.base.Trans import Trans, t
from gdo.core.GDO_Channel import GDO_Channel
from gdo.shadowdogs.GDO_Item import GDO_Item
from gdo.shadowdogs.GDO_Party import GDO_Party
from gdo.shadowdogs.GDO_Player import GDO_Player


class WithShadowFunc:

    def get_player(self) -> 'GDO_Player':
        return GDO_Player.table().get_by_aid(self._env_user.get_id())

    def gdo_default_enabled(cls) -> bool:
        return False

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

    def give_items(self, player: GDO_Player, *item_names: str):
        for item_name in item_names:
            self.give_item(player, item_name)

    def give_item(self, player: GDO_Player, item_name: str, item_count: int):
        item = GDO_Item.create(item_name, item_count, player)
        player.inventory.append(item)
        self.send_to_player(player, 'sd_item_received', (item_name,))
