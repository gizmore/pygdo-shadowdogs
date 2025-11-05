from gdo.shadowdogs.quest.DeliveryQuest import DeliveryQuest

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.city.y2064.Peine.locations.trains.Bum import Bum


class Bottles(DeliveryQuest):

    ITEM_NAMES = "6xBottle"
    TARGET_NPC: 'type[Bum]' = None
