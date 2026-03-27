from gdo.shadowdogs.city.y2064.Peine.locations.car_repair.Peter import Peter
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
from gdo.shadowdogs.quest.DeliveryQuest import DeliveryQuest


class Tired(DeliveryQuest):
    ITEM_NAMES = "8xWheel"
    TARGET_NPC: type[TalkingNPC] = Peter

    def reward_xp(self) -> int:
        return 15
