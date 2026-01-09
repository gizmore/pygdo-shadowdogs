from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.hospital.Doctor import Doctor
from gdo.shadowdogs.locations.Hospital import Hospital as HospitalBase
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Hospital(HospitalBase):

    NPCS: 'list[type[TalkingNPC]]' = [
        Doctor,
    ]

    def sd_cyberware(self, player: SD_Player) -> list[tuple[str, int]]:
        return [
            ('NeuralJackLite', 1200),
            ('CyberEyeI', 1800),
            ('DermalWeaveI', 3600),
            ('MuscleWireI', 3400),
            ('ReflexBoosterI', 4300),
        ]
