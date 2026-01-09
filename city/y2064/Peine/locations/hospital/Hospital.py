from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.locations.Hospital import Hospital as HospitalBase


class Hospital(HospitalBase):

    def sd_cyberware(self, player: SD_Player) -> list[tuple[str, int]]:
        return [
            ('NeuralJackLite', 1200),
            ('CyberEyeI', 1800),
            ('DermalWeaveI', 3600),
            ('MuscleWireI', 3400),
            ('ReflexBoosterI', 4300),
        ]
