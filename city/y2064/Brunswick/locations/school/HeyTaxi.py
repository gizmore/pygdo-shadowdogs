from gdo.date.Time import Time
from gdo.shadowdogs.SD_Quest import SD_Quest


class HeyTaxi(SD_Quest):

    TAXI_COST = 100
    TAXI_TIME = Time.ONE_MINUTE * 30

    @classmethod
    def QUEST_TIME(cls) -> int:
        from gdo.shadowdogs.engine.World import World
        return cls.TAXI_TIME + World.World2064.Peine.get_explore_eta(None) + Time.ONE_MINUTE * 7

    def reward_xp(self) -> int:
        return 8
