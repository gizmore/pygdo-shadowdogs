from gdo.shadowdogs.SD_Quest import SD_Quest


class Carpenter(SD_Quest):

    def reward(self) -> str|None:
        return 'OldSpeaker,Wires,Battery'

    def reward_xp(self) -> int:
        return 2
