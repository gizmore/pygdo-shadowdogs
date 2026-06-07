from gdo.date.Time import Time
from gdo.shadowdogs.SD_Quest import SD_Quest


class TBS(SD_Quest):

    WORK_TIME = Time.ONE_HOUR * 1
    WORK_TIMES = 4

    def reward_xp(self) -> int:
        return 23
