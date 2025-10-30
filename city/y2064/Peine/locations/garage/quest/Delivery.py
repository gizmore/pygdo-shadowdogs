from gdo.shadowdogs.quest.DeliveryQuest import DeliveryQuest
from gdo.shadowdogs.city.y2064.Peine.locations.garage.npc.Barkeeper import Barkeeper


class Delivery(DeliveryQuest):

    BEER_COUNT = 50
    TARGET_NPC = Barkeeper
    ITEM_NAMES = f"{BEER_COUNT}xLargeBeer"

    def reward(self) -> str|None:
        return '50xNuyen'

    def reward_xp(self) -> int:
        return 8
