from gdo.shadowdogs.quest.KillQuest import KillQuest


class Hate(KillQuest):

    NUM_KILLS = 8
    REWARD_NY = 200

    def reward(self) -> str|None:
        return f"{Hate.REWARD_NY}xNuyen"

    KILLS: dict[str, int] = {
        'haider': NUM_KILLS,
    }
