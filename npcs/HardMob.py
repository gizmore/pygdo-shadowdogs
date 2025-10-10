from gdo.shadowdogs.SD_NPC import SD_NPC


class HardMob(SD_NPC):

    def ai_decision(self) -> str:
        return 'sdp'

    async def digesting(self):
        return self
