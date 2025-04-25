from gdo.shadowdogs.SD_NPC import SD_NPC


class Mob(SD_NPC):

    def ai_decision(self) -> str:
        return 'sdp'
