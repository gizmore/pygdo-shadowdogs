from gdo.shadowdogs.SD_NPC import SD_NPC


class Mob(SD_NPC):

    def is_mob(self) -> bool:
        return True

    def ai_decision(self) -> str:
        return 'sdp'

    async def digesting(self):
        return self

    def is_foe(self) -> bool:
        return True
