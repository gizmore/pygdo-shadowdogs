from gdo.date.Time import Time
from gdo.shadowdogs.SD_Quest import SD_Quest


class Plants(SD_Quest):

    WORK_TIMES = 4
    WORK_REWARD = 25
    WORK_TIME = Time.ONE_HOUR * 0.5

    def reward_xp(self) -> int:
        return 4

    def reward(self) -> str|None:
        return "150xNuyen"
