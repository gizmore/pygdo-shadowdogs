from gdo.shadowdogs.quest.DeliveryQuest import DeliveryQuest

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.city.y2064.Peine.npcs.garage.Barkeeper import Barkeeper


class Delivery(DeliveryQuest):

    BEER_COUNT = 50
    TARGET_NPC: 'type[Barkeeper]'
    ITEM_NAMES = f"{BEER_COUNT}xLargeBeer"

    def reward(self) -> str|None:
        return '50xNuyen'

    def reward_xp(self) -> int:
        return 8
