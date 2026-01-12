from gdo.shadowdogs.SD_Quest import SD_Quest


class Carpenter(SD_Quest):

    def reward(self) -> str|None:
        return '2xOldSpeaker'

    def reward_xp(self) -> int:
        return 2
