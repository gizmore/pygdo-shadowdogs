from gdo.shadowdogs.npcs.Mob import Mob


class HardMob(Mob):

    def ai_decision(self) -> str:
        return 'sdp'
