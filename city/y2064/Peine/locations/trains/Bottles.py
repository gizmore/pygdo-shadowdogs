from gdo.shadowdogs.city.y2064.Peine.locations.trains.Bum import Bum
from gdo.shadowdogs.quest.DeliveryQuest import DeliveryQuest


class Bottles(DeliveryQuest):

    ITEM_NAMES = "6xBottle"
    TARGET_NPC: type[Bum] = None
