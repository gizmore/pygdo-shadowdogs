from gdo.shadowdogs.city.y2064.Peine.locations.hospital.Doctor import Doctor
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC
from gdo.shadowdogs.quest.DeliveryQuest import DeliveryQuest


class Aid(DeliveryQuest):
    ITEM_NAMES = "6xFirstAid"
    TARGET_NPC: type[TalkingNPC] = Doctor
